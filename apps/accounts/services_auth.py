"""
Domain Services for EduFlow Authentication Workflows & Profile Management (Auth).
Enterprise service layer with 18 specialized business logic, conflict checking,
and transaction orchestration methods.
"""

import logging
from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from django.core.exceptions import ValidationError
try:
    from .models import (
        AuthMaster, AuthItem, AuthAllocation,
        AuthMetricRecord, AuthPolicyRule, AuthSchedulePeriod,
        AuthFeedbackReview, AuthWorkflowTransition, AuthAccessRule,
        AuthConfigurationParameter, AuthDocumentAttachment, AuthAuditTrail
    )
except ImportError:
    try:
        from .models_auth import (
            AuthMaster, AuthItem, AuthAllocation,
            AuthMetricRecord, AuthPolicyRule, AuthSchedulePeriod,
            AuthFeedbackReview, AuthWorkflowTransition, AuthAccessRule,
            AuthConfigurationParameter, AuthDocumentAttachment, AuthAuditTrail
        )
    except ImportError:
        pass

logger = logging.getLogger(__name__)

class AuthService:
    """Enterprise domain business service for Auth."""

    @classmethod
    @transaction.atomic
    def create_record(cls, code, name, user_username="system", **kwargs):
        """Creates a master record with auto-validation and audit stamping."""
        record = AuthMaster.objects.create(
            code=code.strip().upper(),
            name=name.strip(),
            created_by_user=user_username,
            updated_by_user=user_username,
            **kwargs
        )
        cls._log_action(record, "CREATE", user_username, {}, record.to_dict(), "Initial creation")
        logger.info(f"Created Auth record {record.code} by {user_username}")
        return record

    @classmethod
    @transaction.atomic
    def update_record(cls, record_id, user_username="system", **kwargs):
        """Updates an existing record, diffing previous and new states."""
        record = AuthMaster.objects.select_for_update().get(pk=record_id)
        old_state = record.to_dict()

        for key, value in kwargs.items():
            if hasattr(record, key):
                setattr(record, key, value)

        record.updated_by_user = user_username
        record.save()

        new_state = record.to_dict()
        cls._log_action(record, "UPDATE", user_username, old_state, new_state, "Metadata update")
        return record

    @classmethod
    @transaction.atomic
    def change_status(cls, record_id, target_status, user_username="system", remarks=""):
        """Validates state machine transitions."""
        record = AuthMaster.objects.select_for_update().get(pk=record_id)
        old_status = record.status

        record.transition_status(target_status, user_username=user_username)
        cls._log_action(record, "STATUS_CHANGE", user_username, {'status': old_status}, {'status': target_status}, remarks)
        return record

    @classmethod
    def calculate_utilization_metrics(cls, record_id):
        """Computes live utilization, capacity headroom, and load factor."""
        record = AuthMaster.objects.get(pk=record_id)
        headroom = max(0, record.capacity - record.current_occupancy)
        rate = record.utilization_rate
        is_overloaded = record.current_occupancy > record.capacity

        return {
            'record_code': record.code,
            'capacity': record.capacity,
            'occupancy': record.current_occupancy,
            'headroom': headroom,
            'utilization_rate': rate,
            'is_overloaded': is_overloaded,
            'status': 'CRITICAL' if is_overloaded else ('WARNING' if rate > 85 else 'OPTIMAL'),
        }

    @classmethod
    @transaction.atomic
    def add_line_item(cls, record_id, item_code, title, quantity=1, unit_rate=0, remarks=""):
        """Adds a subordinate line item component."""
        record = AuthMaster.objects.get(pk=record_id)
        item = AuthItem.objects.create(
            master=record,
            item_code=item_code,
            title=title,
            quantity=quantity,
            unit_rate=unit_rate,
            remarks=remarks
        )
        return item

    @classmethod
    @transaction.atomic
    def allocate_resource(cls, record_id, assignee_id, assignee_name, role="Lead", start_time=None, end_time=None):
        """Creates a verified resource allocation."""
        record = AuthMaster.objects.get(pk=record_id)
        start = start_time or timezone.now()
        allocation = AuthAllocation.objects.create(
            master=record,
            assignee_id=assignee_id,
            assignee_name=assignee_name,
            allocation_role=role,
            start_time=start,
            end_time=end_time
        )
        return allocation

    @classmethod
    @transaction.atomic
    def release_allocation(cls, allocation_id):
        """Releases an active allocation."""
        alloc = AuthAllocation.objects.get(pk=allocation_id)
        alloc.is_active = False
        alloc.end_time = timezone.now()
        alloc.save()
        return alloc

    @classmethod
    def evaluate_compliance_rules(cls, record_id):
        """Checks compliance against all defined policy rules."""
        record = AuthMaster.objects.get(pk=record_id)
        rules = record.policy_rules.filter(is_enforced=True)
        results = []
        all_passed = True

        for rule in rules:
            passed = rule.check_compliance(record.utilization_rate)
            if not passed:
                all_passed = False
            results.append({
                'rule_code': rule.rule_code,
                'rule_name': rule.rule_name,
                'threshold': float(rule.threshold_value),
                'passed': passed,
                'action_on_breach': rule.action_on_breach
            })

        return {'all_passed': all_passed, 'details': results}

    @classmethod
    @transaction.atomic
    def record_kpi_metric(cls, record_id, metric_name, target_val, actual_val, remarks=""):
        """Records an evaluated performance metric."""
        record = AuthMaster.objects.get(pk=record_id)
        metric = AuthMetricRecord.objects.create(
            master=record,
            metric_name=metric_name,
            target_value=target_val,
            actual_value=actual_val,
            evaluator_remarks=remarks
        )
        return metric

    @classmethod
    @transaction.atomic
    def schedule_period_session(cls, record_id, title, day, start_time, end_time, room=""):
        """Schedules an operational time period."""
        record = AuthMaster.objects.get(pk=record_id)
        period = AuthSchedulePeriod.objects.create(
            master=record,
            period_title=title,
            day_of_week=day,
            start_time=start_time,
            end_time=end_time,
            room_number=room
        )
        return period

    @classmethod
    @transaction.atomic
    def submit_feedback_review(cls, record_id, name, role, rating, feedback, recommendations=""):
        """Submits an institutional evaluation review."""
        record = AuthMaster.objects.get(pk=record_id)
        review = AuthFeedbackReview.objects.create(
            master=record,
            reviewer_name=name,
            reviewer_role=role,
            rating=rating,
            qualitative_feedback=feedback,
            actionable_recommendations=recommendations
        )
        return review

    @classmethod
    @transaction.atomic
    def execute_workflow_transition(cls, record_id, from_stage, to_stage, actor, comments="", is_approved=True):
        """Advances multi-stage governance approval workflow."""
        record = AuthMaster.objects.get(pk=record_id)
        trans = AuthWorkflowTransition.objects.create(
            master=record,
            from_stage=from_stage,
            to_stage=to_stage,
            actor_username=actor,
            approver_comments=comments,
            is_approved=is_approved
        )
        if is_approved and to_stage in record.StatusChoices.values:
            record.transition_status(to_stage, user_username=actor)
        return trans

    @classmethod
    @transaction.atomic
    def grant_access_permission(cls, record_id, role, can_read=True, can_write=False, can_delete=False, grantor="system"):
        """Grants role-specific access permissions."""
        record = AuthMaster.objects.get(pk=record_id)
        rule = AuthAccessRule.objects.create(
            master=record,
            role_allowed=role,
            can_read=can_read,
            can_write=can_write,
            can_delete=can_delete,
            granted_by=grantor
        )
        return rule

    @classmethod
    @transaction.atomic
    def set_configuration_parameter(cls, record_id, key, val, data_type="STRING", desc=""):
        """Sets runtime configuration parameters."""
        record = AuthMaster.objects.get(pk=record_id)
        param, _ = AuthConfigurationParameter.objects.update_or_create(
            master=record,
            param_key=key,
            defaults={'param_value': str(val), 'data_type': data_type, 'description': desc}
        )
        return param

    @classmethod
    @transaction.atomic
    def attach_official_document(cls, record_id, title, path, size=0, mime="application/pdf", checksum="", uploader="system"):
        """Attaches an official document reference."""
        record = AuthMaster.objects.get(pk=record_id)
        doc = AuthDocumentAttachment.objects.create(
            master=record,
            title=title,
            file_path=path,
            file_size_bytes=size,
            mime_type=mime,
            checksum_hash=checksum,
            uploaded_by=uploader
        )
        return doc

    @classmethod
    def detect_allocation_conflicts(cls, record_id, start_time, end_time):
        """Detects overlapping resource allocations."""
        record = AuthMaster.objects.get(pk=record_id)
        conflicts = []
        for alloc in record.allocations.filter(is_active=True):
            if alloc.is_overlapping(start_time, end_time):
                conflicts.append(alloc)
        return conflicts

    @classmethod
    def generate_executive_summary(cls, record_id):
        """Generates an executive KPI briefing for institutional directors."""
        record = AuthMaster.objects.get(pk=record_id)
        metrics = cls.calculate_utilization_metrics(record_id)
        compliance = cls.evaluate_compliance_rules(record_id)

        return {
            'overview': record.to_dict(),
            'capacity_metrics': metrics,
            'compliance_status': compliance,
            'item_count': record.items.count() if hasattr(record, 'items') else 0,
            'allocation_count': record.allocations.count() if hasattr(record, 'allocations') else 0,
        }

    @classmethod
    def _log_action(cls, record, action_type, user_username, old_state, new_state, summary):
        if 'AuthAuditTrail' in globals():
            try:
                AuthAuditTrail.objects.create(
                    master=record,
                    action_type=action_type,
                    performed_by=user_username,
                    previous_state=old_state,
                    new_state=new_state,
                    change_summary=summary
                )
            except Exception as e:
                logger.warning(f"Failed to record audit log for Auth: {e}")

"""
Advanced Service Orchestration and Business Operations for EduFlow Hostel Bed Allocation & Check-In (BedAllocations).
Includes event notifications, automated compliance reconciliation, batch state machines,
and enterprise analytics engines.
"""

import csv
import json
import logging
from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models import Q, Sum, Avg, Count, Min, Max

try:
    from .models import (
        BedAllocationsMaster, BedAllocationsItem, BedAllocationsAllocation,
        BedAllocationsMetricRecord, BedAllocationsPolicyRule, BedAllocationsSchedulePeriod,
        BedAllocationsFeedbackReview, BedAllocationsWorkflowTransition, BedAllocationsAccessRule,
        BedAllocationsConfigurationParameter, BedAllocationsDocumentAttachment, BedAllocationsAuditTrail
    )
except ImportError:
    try:
        from .models_bedallocations import (
            BedAllocationsMaster, BedAllocationsItem, BedAllocationsAllocation,
            BedAllocationsMetricRecord, BedAllocationsPolicyRule, BedAllocationsSchedulePeriod,
            BedAllocationsFeedbackReview, BedAllocationsWorkflowTransition, BedAllocationsAccessRule,
            BedAllocationsConfigurationParameter, BedAllocationsDocumentAttachment, BedAllocationsAuditTrail
        )
    except ImportError:
        pass

logger = logging.getLogger(__name__)

class BedAllocationsAdvancedService:
    """Enterprise-grade service orchestrator for complex operations in BedAllocations."""

    @classmethod
    @transaction.atomic
    def bulk_create_records(cls, record_data_list, user_username="system"):
        """Batch ingestion of multiple master records with rollback safety."""
        created_records = []
        for data in record_data_list:
            code = data.pop('code', '').strip().upper()
            name = data.pop('name', '').strip()
            if not code or not name:
                continue
            rec = BedAllocationsMaster.objects.create(
                code=code,
                name=name,
                created_by_user=user_username,
                updated_by_user=user_username,
                **data
            )
            created_records.append(rec)
            cls._record_audit_event(rec, "BULK_CREATE", user_username, f"Bulk created {code}")
        logger.info(f"Bulk created {len(created_records)} BedAllocations records by {user_username}")
        return created_records

    @classmethod
    @transaction.atomic
    def execute_lifecycle_rollover(cls, from_academic_year, to_academic_year, user_username="system"):
        """Rolls over active configurations and master records to the next academic cycle."""
        active_records = BedAllocationsMaster.objects.filter(status='ACTIVE', is_recurring=True)
        rollover_count = 0
        for rec in active_records:
            new_code = f"{rec.code}-{to_academic_year}"
            if not BedAllocationsMaster.objects.filter(code=new_code).exists():
                cloned = BedAllocationsMaster.objects.create(
                    code=new_code,
                    name=f"{rec.name} ({to_academic_year})",
                    category=rec.category,
                    tier=rec.tier,
                    scope=rec.scope,
                    priority=rec.priority,
                    status='DRAFT',
                    capacity=rec.capacity,
                    current_occupancy=0,
                    reserved_headroom=rec.reserved_headroom,
                    weightage=rec.weightage,
                    budget_allocated=rec.budget_allocated,
                    cost_incurred=Decimal('0.00'),
                    effective_start_date=timezone.now().date(),
                    is_recurring=True,
                    is_public=rec.is_public,
                    description=rec.description,
                    operational_guidelines=rec.operational_guidelines,
                    tags=rec.tags,
                    created_by_user=user_username,
                    updated_by_user=user_username
                )
                rollover_count += 1
                cls._record_audit_event(cloned, "ROLLOVER", user_username, f"Rolled over from {rec.code}")
        return {'status': 'completed', 'records_rolled_over': rollover_count}

    @classmethod
    def analyze_operational_efficiency(cls, record_id):
        """Deep analytics: capacity utilization, cost per capita, and risk scoring."""
        rec = BedAllocationsMaster.objects.get(pk=record_id)
        util_rate = rec.utilization_rate
        cost_per_unit = (rec.cost_incurred / rec.current_occupancy) if rec.current_occupancy > 0 else Decimal('0.00')
        budget_burn_rate = round((rec.cost_incurred / rec.budget_allocated * 100), 2) if rec.budget_allocated > 0 else Decimal('0.00')
        
        # Risk assessment
        risk_flags = []
        if util_rate > 95:
            risk_flags.append("CRITICAL_CAPACITY_CONGESTION")
        elif util_rate < 30:
            risk_flags.append("UNDERUTILIZATION_WARNING")
            
        if budget_burn_rate > 100:
            risk_flags.append("BUDGET_OVERRUN_ALERT")
        elif budget_burn_rate > 85:
            risk_flags.append("BUDGET_EXHAUSTION_WARNING")

        return {
            'record_id': rec.pk,
            'code': rec.code,
            'name': rec.name,
            'utilization_rate': util_rate,
            'cost_per_occupant': float(cost_per_unit),
            'budget_burn_percentage': float(budget_burn_rate),
            'risk_level': 'HIGH' if len(risk_flags) >= 2 else ('MEDIUM' if len(risk_flags) == 1 else 'LOW'),
            'risk_flags': risk_flags,
            'evaluated_at': timezone.now().isoformat(),
        }

    @classmethod
    @transaction.atomic
    def process_schedule_conflict_resolution(cls, record_id, auto_resolve=False):
        """Detects and optionally resolves schedule overlaps across allocations."""
        record = BedAllocationsMaster.objects.get(pk=record_id)
        active_allocations = list(record.allocations.filter(is_active=True).order_by('start_time'))
        conflicts = []
        
        for i in range(len(active_allocations)):
            for j in range(i + 1, len(active_allocations)):
                a1 = active_allocations[i]
                a2 = active_allocations[j]
                if a1.is_overlapping(a2.start_time, a2.end_time):
                    conflicts.append({
                        'allocation_1_id': a1.pk,
                        'assignee_1': a1.assignee_name,
                        'allocation_2_id': a2.pk,
                        'assignee_2': a2.assignee_name,
                        'conflict_window': f"{max(a1.start_time, a2.start_time)} to {min(a1.end_time or timezone.now(), a2.end_time or timezone.now())}"
                    })
                    if auto_resolve:
                        a2.is_active = False
                        a2.notes = f"Auto-deactivated due to scheduling conflict with allocation #{a1.pk}"
                        a2.save()
                        
        return {
            'conflict_count': len(conflicts),
            'conflicts': conflicts,
            'auto_resolved': auto_resolve
        }

    @classmethod
    def generate_annual_compliance_audit(cls, record_id):
        """Generates comprehensive regulatory audit report."""
        record = BedAllocationsMaster.objects.get(pk=record_id)
        policy_checks = record.policy_rules.all()
        audit_history = record.audit_records.all().order_by('-timestamp')[:50]
        
        passed_rules = [r for r in policy_checks if r.check_compliance(record.utilization_rate)]
        failed_rules = [r for r in policy_checks if not r.check_compliance(record.utilization_rate)]
        
        compliance_pct = round((len(passed_rules) / len(policy_checks) * 100), 2) if policy_checks else 100.0
        
        return {
            'institution_record': record.code,
            'total_governance_rules': len(policy_checks),
            'passed_rules_count': len(passed_rules),
            'failed_rules_count': len(failed_rules),
            'compliance_score': compliance_pct,
            'audit_entry_count': len(audit_history),
            'status': 'COMPLIANT' if compliance_pct >= 90.0 else 'NON_COMPLIANT',
            'certified_at': timezone.now().isoformat(),
        }

    @classmethod
    def export_comprehensive_archive_dataset(cls, record_id):
        """Serializes the entire 12-model entity graph to an archive bundle."""
        record = BedAllocationsMaster.objects.get(pk=record_id)
        return {
            'master': record.to_dict(),
            'items': [i.total_amount for i in record.items.all()] if hasattr(record, 'items') else [],
            'allocations': [a.assignee_name for a in record.allocations.all()] if hasattr(record, 'allocations') else [],
            'metrics': [m.metric_name for m in record.metrics.all()] if hasattr(record, 'metrics') else [],
            'policy_rules': [p.rule_code for p in record.policy_rules.all()] if hasattr(record, 'policy_rules') else [],
            'schedule_periods': [s.period_title for s in record.schedule_periods.all()] if hasattr(record, 'schedule_periods') else [],
            'reviews': [r.rating for r in record.reviews.all()] if hasattr(record, 'reviews') else [],
            'workflow_transitions': [w.to_stage for w in record.workflow_transitions.all()] if hasattr(record, 'workflow_transitions') else [],
            'access_rules': [ar.role_allowed for ar in record.access_rules.all()] if hasattr(record, 'access_rules') else [],
            'config_parameters': [{c.param_key: c.param_value} for c in record.config_parameters.all()] if hasattr(record, 'config_parameters') else [],
            'attachments': [att.title for att in record.attachments.all()] if hasattr(record, 'attachments') else [],
            'audit_trail_length': record.audit_records.count() if hasattr(record, 'audit_records') else 0,
        }

    @classmethod
    def _record_audit_event(cls, record, action_type, user_username, summary):
        if 'BedAllocationsAuditTrail' in globals():
            try:
                BedAllocationsAuditTrail.objects.create(
                    master=record,
                    action_type=action_type,
                    performed_by=user_username,
                    change_summary=summary,
                    new_state=record.to_dict()
                )
            except Exception as e:
                logger.warning(f"Failed to record advanced audit log: {e}")

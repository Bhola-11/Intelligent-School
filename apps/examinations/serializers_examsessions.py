"""
Serializers for EduFlow Examination Sessions & Exam Types (ExamSessions).
Provides serialization, deserialization, and schema validation for all domain entities.
"""

import json
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

try:
    from .models import (
        ExamSessionsMaster, ExamSessionsItem, ExamSessionsAllocation,
        ExamSessionsMetricRecord, ExamSessionsPolicyRule, ExamSessionsSchedulePeriod,
        ExamSessionsFeedbackReview, ExamSessionsWorkflowTransition, ExamSessionsAccessRule,
        ExamSessionsConfigurationParameter, ExamSessionsDocumentAttachment, ExamSessionsAuditTrail
    )
except ImportError:
    pass

class ExamSessionsMasterSerializer:
    """Serializes ExamSessionsMaster instances to and from JSON/dict structures."""
    
    @classmethod
    def serialize(cls, instance):
        if not instance:
            return None
        return {
            'uuid': str(instance.uuid),
            'code': instance.code,
            'name': instance.name,
            'short_name': instance.short_name,
            'category': instance.category,
            'tier': instance.tier,
            'scope': instance.scope,
            'priority': instance.priority,
            'status': instance.status,
            'capacity': instance.capacity,
            'current_occupancy': instance.current_occupancy,
            'utilization_rate': instance.utilization_rate,
            'remaining_headroom': instance.remaining_headroom,
            'budget_allocated': float(instance.budget_allocated),
            'cost_incurred': float(instance.cost_incurred),
            'net_budget_variance': float(instance.net_budget_variance),
            'effective_start_date': str(instance.effective_start_date),
            'effective_end_date': str(instance.effective_end_date) if instance.effective_end_date else None,
            'is_recurring': instance.is_recurring,
            'is_public': instance.is_public,
            'is_locked': instance.is_locked,
            'tags': instance.tags,
            'created_at': instance.created_at.isoformat() if instance.created_at else None,
            'updated_at': instance.updated_at.isoformat() if instance.updated_at else None,
        }

    @classmethod
    def serialize_many(cls, queryset):
        return [cls.serialize(item) for item in queryset]

    @classmethod
    def validate_payload(cls, data):
        errors = {}
        if not data.get('code'):
            errors['code'] = _("Code is mandatory.")
        elif len(data['code']) < 3:
            errors['code'] = _("Code must be at least 3 characters.")
        
        if not data.get('name'):
            errors['name'] = _("Name is mandatory.")

        if 'capacity' in data and int(data['capacity']) <= 0:
            errors['capacity'] = _("Capacity must be positive.")

        if errors:
            raise ValidationError(errors)
        return True


class ExamSessionsItemSerializer:
    @classmethod
    def serialize(cls, item):
        return {
            'id': item.id,
            'item_code': item.item_code,
            'title': item.title,
            'sequence_order': item.sequence_order,
            'quantity': float(item.quantity),
            'unit_rate': float(item.unit_rate),
            'total_amount': float(item.total_amount),
            'is_mandatory': item.is_mandatory,
            'is_completed': item.is_completed,
            'completion_date': item.completion_date.isoformat() if item.completion_date else None,
            'remarks': item.remarks,
        }


class ExamSessionsAllocationSerializer:
    @classmethod
    def serialize(cls, alloc):
        return {
            'id': alloc.id,
            'assignee_id': alloc.assignee_id,
            'assignee_name': alloc.assignee_name,
            'allocation_role': alloc.allocation_role,
            'start_time': alloc.start_time.isoformat() if alloc.start_time else None,
            'end_time': alloc.end_time.isoformat() if alloc.end_time else None,
            'allocated_quota': alloc.allocated_quota,
            'is_active': alloc.is_active,
            'authorization_code': alloc.authorization_code,
        }


class ExamSessionsMetricSerializer:
    @classmethod
    def serialize(cls, metric):
        return {
            'id': metric.id,
            'metric_name': metric.metric_name,
            'target_value': float(metric.target_value),
            'actual_value': float(metric.actual_value),
            'score_percentage': float(metric.score_percentage),
            'is_passing': metric.is_passing,
            'evaluated_at': metric.evaluated_at.isoformat() if metric.evaluated_at else None,
        }

class ExamSessionsPolicyRuleSerializer:
    @classmethod
    def serialize(cls, rule):
        return {
            'id': rule.id,
            'rule_code': rule.rule_code,
            'rule_name': rule.rule_name,
            'threshold_value': float(rule.threshold_value),
            'comparison_operator': rule.comparison_operator,
            'action_on_breach': rule.action_on_breach,
            'is_enforced': rule.is_enforced,
            'rule_description': rule.rule_description,
        }

class ExamSessionsSchedulePeriodSerializer:
    @classmethod
    def serialize(cls, period):
        return {
            'id': period.id,
            'period_title': period.period_title,
            'day_of_week': period.day_of_week,
            'start_time': period.start_time.isoformat() if period.start_time else None,
            'end_time': period.end_time.isoformat() if period.end_time else None,
            'is_break_period': period.is_break_period,
            'room_number': period.room_number,
        }

class ExamSessionsFeedbackReviewSerializer:
    @classmethod
    def serialize(cls, review):
        return {
            'id': review.id,
            'reviewer_role': review.reviewer_role,
            'reviewer_name': review.reviewer_name,
            'rating': review.rating,
            'qualitative_feedback': review.qualitative_feedback,
            'actionable_recommendations': review.actionable_recommendations,
            'is_resolved': review.is_resolved,
            'submitted_at': review.submitted_at.isoformat() if review.submitted_at else None,
        }

class ExamSessionsWorkflowTransitionSerializer:
    @classmethod
    def serialize(cls, wf):
        return {
            'id': wf.id,
            'from_stage': wf.from_stage,
            'to_stage': wf.to_stage,
            'actor_username': wf.actor_username,
            'approver_comments': wf.approver_comments,
            'is_approved': wf.is_approved,
            'transition_timestamp': wf.transition_timestamp.isoformat() if wf.transition_timestamp else None,
        }

class ExamSessionsAccessRuleSerializer:
    @classmethod
    def serialize(cls, rule):
        return {
            'id': rule.id,
            'role_allowed': rule.role_allowed,
            'can_read': rule.can_read,
            'can_write': rule.can_write,
            'can_delete': rule.can_delete,
            'can_export': rule.can_export,
        }

class ExamSessionsConfigurationParameterSerializer:
    @classmethod
    def serialize(cls, param):
        return {
            'id': param.id,
            'param_key': param.param_key,
            'param_value': param.param_value,
            'data_type': param.data_type,
            'is_editable': param.is_editable,
            'description': param.description,
        }

class ExamSessionsDocumentAttachmentSerializer:
    @classmethod
    def serialize(cls, doc):
        return {
            'id': doc.id,
            'title': doc.title,
            'file_path': doc.file_path,
            'file_size_bytes': doc.file_size_bytes,
            'mime_type': doc.mime_type,
            'uploaded_by': doc.uploaded_by,
            'uploaded_at': doc.uploaded_at.isoformat() if doc.uploaded_at else None,
        }

class ExamSessionsAuditTrailSerializer:
    @classmethod
    def serialize(cls, audit):
        return {
            'id': audit.id,
            'action_type': audit.action_type,
            'performed_by': audit.performed_by,
            'ip_address': audit.ip_address,
            'change_summary': audit.change_summary,
            'timestamp': audit.timestamp.isoformat() if audit.timestamp else None,
        }

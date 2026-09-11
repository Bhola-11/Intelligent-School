"""Django Admin configuration for EduFlow Admissions Entrance Exams & Interviews (EntranceExam)."""
from django.contrib import admin
try:
    from .models import (
        EntranceExamMaster, EntranceExamItem, EntranceExamAllocation,
        EntranceExamMetricRecord, EntranceExamPolicyRule, EntranceExamSchedulePeriod,
        EntranceExamFeedbackReview, EntranceExamWorkflowTransition, EntranceExamAccessRule,
        EntranceExamConfigurationParameter, EntranceExamDocumentAttachment, EntranceExamAuditTrail
    )
except ImportError:
    try:
        from .models_entranceexam import (
            EntranceExamMaster, EntranceExamItem, EntranceExamAllocation,
            EntranceExamMetricRecord, EntranceExamPolicyRule, EntranceExamSchedulePeriod,
            EntranceExamFeedbackReview, EntranceExamWorkflowTransition, EntranceExamAccessRule,
            EntranceExamConfigurationParameter, EntranceExamDocumentAttachment, EntranceExamAuditTrail
        )
    except ImportError:
        pass

if 'EntranceExamMaster' in globals():
    @admin.register(EntranceExamMaster)
    class EntranceExamMasterAdmin(admin.ModelAdmin):
        list_display = ['code', 'name', 'category', 'tier', 'priority', 'status', 'capacity', 'current_occupancy', 'created_at']
        list_filter = ['status', 'priority', 'tier', 'category', 'created_at']
        search_fields = ['code', 'name', 'description', 'tags']
        readonly_fields = ['uuid', 'created_at', 'updated_at']
        fieldsets = (
            ('Primary Information', {'fields': ('uuid', 'code', 'name', 'short_name', 'category', 'tier', 'scope', 'status', 'priority')}),
            ('Capacity & Financials', {'fields': ('capacity', 'current_occupancy', 'reserved_headroom', 'weightage', 'budget_allocated', 'cost_incurred')}),
            ('Temporal Bounds', {'fields': ('effective_start_date', 'effective_end_date', 'is_recurring', 'is_public', 'is_locked', 'requires_director_approval')}),
            ('Scope & Content', {'fields': ('description', 'operational_guidelines', 'internal_notes', 'tags', 'attributes')}),
            ('Audit Stamp', {'fields': ('created_by_user', 'updated_by_user', 'created_at', 'updated_at')}),
        )

if 'EntranceExamItem' in globals():
    @admin.register(EntranceExamItem)
    class EntranceExamItemAdmin(admin.ModelAdmin):
        list_display = ['master', 'item_code', 'title', 'quantity', 'unit_rate', 'total_amount', 'is_completed']
        list_filter = ['is_completed', 'is_mandatory']
        search_fields = ['item_code', 'title']

if 'EntranceExamAllocation' in globals():
    @admin.register(EntranceExamAllocation)
    class EntranceExamAllocationAdmin(admin.ModelAdmin):
        list_display = ['master', 'assignee_name', 'allocation_role', 'start_time', 'end_time', 'is_active']
        list_filter = ['is_active', 'allocation_role']
        search_fields = ['assignee_name', 'authorization_code']

if 'EntranceExamMetricRecord' in globals():
    @admin.register(EntranceExamMetricRecord)
    class EntranceExamMetricRecordAdmin(admin.ModelAdmin):
        list_display = ['master', 'metric_name', 'target_value', 'actual_value', 'score_percentage', 'is_passing']
        list_filter = ['is_passing']

if 'EntranceExamPolicyRule' in globals():
    @admin.register(EntranceExamPolicyRule)
    class EntranceExamPolicyRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'rule_code', 'rule_name', 'threshold_value', 'is_enforced']
        list_filter = ['is_enforced']

if 'EntranceExamSchedulePeriod' in globals():
    @admin.register(EntranceExamSchedulePeriod)
    class EntranceExamSchedulePeriodAdmin(admin.ModelAdmin):
        list_display = ['master', 'period_title', 'day_of_week', 'start_time', 'end_time', 'room_number']
        list_filter = ['day_of_week', 'is_break_period']

if 'EntranceExamFeedbackReview' in globals():
    @admin.register(EntranceExamFeedbackReview)
    class EntranceExamFeedbackReviewAdmin(admin.ModelAdmin):
        list_display = ['master', 'reviewer_name', 'reviewer_role', 'rating', 'is_resolved', 'submitted_at']
        list_filter = ['rating', 'is_resolved']

if 'EntranceExamWorkflowTransition' in globals():
    @admin.register(EntranceExamWorkflowTransition)
    class EntranceExamWorkflowTransitionAdmin(admin.ModelAdmin):
        list_display = ['master', 'from_stage', 'to_stage', 'actor_username', 'is_approved', 'transition_timestamp']
        list_filter = ['is_approved']

if 'EntranceExamAccessRule' in globals():
    @admin.register(EntranceExamAccessRule)
    class EntranceExamAccessRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'role_allowed', 'can_read', 'can_write', 'can_delete', 'can_export']
        list_filter = ['role_allowed']

if 'EntranceExamConfigurationParameter' in globals():
    @admin.register(EntranceExamConfigurationParameter)
    class EntranceExamConfigurationParameterAdmin(admin.ModelAdmin):
        list_display = ['master', 'param_key', 'param_value', 'data_type', 'is_editable']

if 'EntranceExamDocumentAttachment' in globals():
    @admin.register(EntranceExamDocumentAttachment)
    class EntranceExamDocumentAttachmentAdmin(admin.ModelAdmin):
        list_display = ['master', 'title', 'mime_type', 'file_size_bytes', 'uploaded_by', 'uploaded_at']

if 'EntranceExamAuditTrail' in globals():
    @admin.register(EntranceExamAuditTrail)
    class EntranceExamAuditTrailAdmin(admin.ModelAdmin):
        list_display = ['master', 'action_type', 'performed_by', 'timestamp']
        list_filter = ['action_type', 'timestamp']
        readonly_fields = ['master', 'action_type', 'performed_by', 'previous_state', 'new_state', 'timestamp', 'change_summary']

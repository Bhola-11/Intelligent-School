"""Django Admin configuration for EduFlow Staff Performance Appraisals & Reviews (Appraisal)."""
from django.contrib import admin
try:
    from .models import (
        AppraisalMaster, AppraisalItem, AppraisalAllocation,
        AppraisalMetricRecord, AppraisalPolicyRule, AppraisalSchedulePeriod,
        AppraisalFeedbackReview, AppraisalWorkflowTransition, AppraisalAccessRule,
        AppraisalConfigurationParameter, AppraisalDocumentAttachment, AppraisalAuditTrail
    )
except ImportError:
    try:
        from .models_appraisal import (
            AppraisalMaster, AppraisalItem, AppraisalAllocation,
            AppraisalMetricRecord, AppraisalPolicyRule, AppraisalSchedulePeriod,
            AppraisalFeedbackReview, AppraisalWorkflowTransition, AppraisalAccessRule,
            AppraisalConfigurationParameter, AppraisalDocumentAttachment, AppraisalAuditTrail
        )
    except ImportError:
        pass

if 'AppraisalMaster' in globals():
    @admin.register(AppraisalMaster)
    class AppraisalMasterAdmin(admin.ModelAdmin):
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

if 'AppraisalItem' in globals():
    @admin.register(AppraisalItem)
    class AppraisalItemAdmin(admin.ModelAdmin):
        list_display = ['master', 'item_code', 'title', 'quantity', 'unit_rate', 'total_amount', 'is_completed']
        list_filter = ['is_completed', 'is_mandatory']
        search_fields = ['item_code', 'title']

if 'AppraisalAllocation' in globals():
    @admin.register(AppraisalAllocation)
    class AppraisalAllocationAdmin(admin.ModelAdmin):
        list_display = ['master', 'assignee_name', 'allocation_role', 'start_time', 'end_time', 'is_active']
        list_filter = ['is_active', 'allocation_role']
        search_fields = ['assignee_name', 'authorization_code']

if 'AppraisalMetricRecord' in globals():
    @admin.register(AppraisalMetricRecord)
    class AppraisalMetricRecordAdmin(admin.ModelAdmin):
        list_display = ['master', 'metric_name', 'target_value', 'actual_value', 'score_percentage', 'is_passing']
        list_filter = ['is_passing']

if 'AppraisalPolicyRule' in globals():
    @admin.register(AppraisalPolicyRule)
    class AppraisalPolicyRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'rule_code', 'rule_name', 'threshold_value', 'is_enforced']
        list_filter = ['is_enforced']

if 'AppraisalSchedulePeriod' in globals():
    @admin.register(AppraisalSchedulePeriod)
    class AppraisalSchedulePeriodAdmin(admin.ModelAdmin):
        list_display = ['master', 'period_title', 'day_of_week', 'start_time', 'end_time', 'room_number']
        list_filter = ['day_of_week', 'is_break_period']

if 'AppraisalFeedbackReview' in globals():
    @admin.register(AppraisalFeedbackReview)
    class AppraisalFeedbackReviewAdmin(admin.ModelAdmin):
        list_display = ['master', 'reviewer_name', 'reviewer_role', 'rating', 'is_resolved', 'submitted_at']
        list_filter = ['rating', 'is_resolved']

if 'AppraisalWorkflowTransition' in globals():
    @admin.register(AppraisalWorkflowTransition)
    class AppraisalWorkflowTransitionAdmin(admin.ModelAdmin):
        list_display = ['master', 'from_stage', 'to_stage', 'actor_username', 'is_approved', 'transition_timestamp']
        list_filter = ['is_approved']

if 'AppraisalAccessRule' in globals():
    @admin.register(AppraisalAccessRule)
    class AppraisalAccessRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'role_allowed', 'can_read', 'can_write', 'can_delete', 'can_export']
        list_filter = ['role_allowed']

if 'AppraisalConfigurationParameter' in globals():
    @admin.register(AppraisalConfigurationParameter)
    class AppraisalConfigurationParameterAdmin(admin.ModelAdmin):
        list_display = ['master', 'param_key', 'param_value', 'data_type', 'is_editable']

if 'AppraisalDocumentAttachment' in globals():
    @admin.register(AppraisalDocumentAttachment)
    class AppraisalDocumentAttachmentAdmin(admin.ModelAdmin):
        list_display = ['master', 'title', 'mime_type', 'file_size_bytes', 'uploaded_by', 'uploaded_at']

if 'AppraisalAuditTrail' in globals():
    @admin.register(AppraisalAuditTrail)
    class AppraisalAuditTrailAdmin(admin.ModelAdmin):
        list_display = ['master', 'action_type', 'performed_by', 'timestamp']
        list_filter = ['action_type', 'timestamp']
        readonly_fields = ['master', 'action_type', 'performed_by', 'previous_state', 'new_state', 'timestamp', 'change_summary']

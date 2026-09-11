"""Django Admin configuration for EduFlow Student Enrollment & Academic History (Enrollment)."""
from django.contrib import admin
try:
    from .models import (
        EnrollmentMaster, EnrollmentItem, EnrollmentAllocation,
        EnrollmentMetricRecord, EnrollmentPolicyRule, EnrollmentSchedulePeriod,
        EnrollmentFeedbackReview, EnrollmentWorkflowTransition, EnrollmentAccessRule,
        EnrollmentConfigurationParameter, EnrollmentDocumentAttachment, EnrollmentAuditTrail
    )
except ImportError:
    try:
        from .models_enrollment import (
            EnrollmentMaster, EnrollmentItem, EnrollmentAllocation,
            EnrollmentMetricRecord, EnrollmentPolicyRule, EnrollmentSchedulePeriod,
            EnrollmentFeedbackReview, EnrollmentWorkflowTransition, EnrollmentAccessRule,
            EnrollmentConfigurationParameter, EnrollmentDocumentAttachment, EnrollmentAuditTrail
        )
    except ImportError:
        pass

if 'EnrollmentMaster' in globals():
    @admin.register(EnrollmentMaster)
    class EnrollmentMasterAdmin(admin.ModelAdmin):
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

if 'EnrollmentItem' in globals():
    @admin.register(EnrollmentItem)
    class EnrollmentItemAdmin(admin.ModelAdmin):
        list_display = ['master', 'item_code', 'title', 'quantity', 'unit_rate', 'total_amount', 'is_completed']
        list_filter = ['is_completed', 'is_mandatory']
        search_fields = ['item_code', 'title']

if 'EnrollmentAllocation' in globals():
    @admin.register(EnrollmentAllocation)
    class EnrollmentAllocationAdmin(admin.ModelAdmin):
        list_display = ['master', 'assignee_name', 'allocation_role', 'start_time', 'end_time', 'is_active']
        list_filter = ['is_active', 'allocation_role']
        search_fields = ['assignee_name', 'authorization_code']

if 'EnrollmentMetricRecord' in globals():
    @admin.register(EnrollmentMetricRecord)
    class EnrollmentMetricRecordAdmin(admin.ModelAdmin):
        list_display = ['master', 'metric_name', 'target_value', 'actual_value', 'score_percentage', 'is_passing']
        list_filter = ['is_passing']

if 'EnrollmentPolicyRule' in globals():
    @admin.register(EnrollmentPolicyRule)
    class EnrollmentPolicyRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'rule_code', 'rule_name', 'threshold_value', 'is_enforced']
        list_filter = ['is_enforced']

if 'EnrollmentSchedulePeriod' in globals():
    @admin.register(EnrollmentSchedulePeriod)
    class EnrollmentSchedulePeriodAdmin(admin.ModelAdmin):
        list_display = ['master', 'period_title', 'day_of_week', 'start_time', 'end_time', 'room_number']
        list_filter = ['day_of_week', 'is_break_period']

if 'EnrollmentFeedbackReview' in globals():
    @admin.register(EnrollmentFeedbackReview)
    class EnrollmentFeedbackReviewAdmin(admin.ModelAdmin):
        list_display = ['master', 'reviewer_name', 'reviewer_role', 'rating', 'is_resolved', 'submitted_at']
        list_filter = ['rating', 'is_resolved']

if 'EnrollmentWorkflowTransition' in globals():
    @admin.register(EnrollmentWorkflowTransition)
    class EnrollmentWorkflowTransitionAdmin(admin.ModelAdmin):
        list_display = ['master', 'from_stage', 'to_stage', 'actor_username', 'is_approved', 'transition_timestamp']
        list_filter = ['is_approved']

if 'EnrollmentAccessRule' in globals():
    @admin.register(EnrollmentAccessRule)
    class EnrollmentAccessRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'role_allowed', 'can_read', 'can_write', 'can_delete', 'can_export']
        list_filter = ['role_allowed']

if 'EnrollmentConfigurationParameter' in globals():
    @admin.register(EnrollmentConfigurationParameter)
    class EnrollmentConfigurationParameterAdmin(admin.ModelAdmin):
        list_display = ['master', 'param_key', 'param_value', 'data_type', 'is_editable']

if 'EnrollmentDocumentAttachment' in globals():
    @admin.register(EnrollmentDocumentAttachment)
    class EnrollmentDocumentAttachmentAdmin(admin.ModelAdmin):
        list_display = ['master', 'title', 'mime_type', 'file_size_bytes', 'uploaded_by', 'uploaded_at']

if 'EnrollmentAuditTrail' in globals():
    @admin.register(EnrollmentAuditTrail)
    class EnrollmentAuditTrailAdmin(admin.ModelAdmin):
        list_display = ['master', 'action_type', 'performed_by', 'timestamp']
        list_filter = ['action_type', 'timestamp']
        readonly_fields = ['master', 'action_type', 'performed_by', 'previous_state', 'new_state', 'timestamp', 'change_summary']

"""Django Admin configuration for EduFlow Staff Leave Applications & Approval Workflows (StaffLeaves)."""
from django.contrib import admin
try:
    from .models import (
        StaffLeavesMaster, StaffLeavesItem, StaffLeavesAllocation,
        StaffLeavesMetricRecord, StaffLeavesPolicyRule, StaffLeavesSchedulePeriod,
        StaffLeavesFeedbackReview, StaffLeavesWorkflowTransition, StaffLeavesAccessRule,
        StaffLeavesConfigurationParameter, StaffLeavesDocumentAttachment, StaffLeavesAuditTrail
    )
except ImportError:
    try:
        from .models_staffleaves import (
            StaffLeavesMaster, StaffLeavesItem, StaffLeavesAllocation,
            StaffLeavesMetricRecord, StaffLeavesPolicyRule, StaffLeavesSchedulePeriod,
            StaffLeavesFeedbackReview, StaffLeavesWorkflowTransition, StaffLeavesAccessRule,
            StaffLeavesConfigurationParameter, StaffLeavesDocumentAttachment, StaffLeavesAuditTrail
        )
    except ImportError:
        pass

if 'StaffLeavesMaster' in globals():
    @admin.register(StaffLeavesMaster)
    class StaffLeavesMasterAdmin(admin.ModelAdmin):
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

if 'StaffLeavesItem' in globals():
    @admin.register(StaffLeavesItem)
    class StaffLeavesItemAdmin(admin.ModelAdmin):
        list_display = ['master', 'item_code', 'title', 'quantity', 'unit_rate', 'total_amount', 'is_completed']
        list_filter = ['is_completed', 'is_mandatory']
        search_fields = ['item_code', 'title']

if 'StaffLeavesAllocation' in globals():
    @admin.register(StaffLeavesAllocation)
    class StaffLeavesAllocationAdmin(admin.ModelAdmin):
        list_display = ['master', 'assignee_name', 'allocation_role', 'start_time', 'end_time', 'is_active']
        list_filter = ['is_active', 'allocation_role']
        search_fields = ['assignee_name', 'authorization_code']

if 'StaffLeavesMetricRecord' in globals():
    @admin.register(StaffLeavesMetricRecord)
    class StaffLeavesMetricRecordAdmin(admin.ModelAdmin):
        list_display = ['master', 'metric_name', 'target_value', 'actual_value', 'score_percentage', 'is_passing']
        list_filter = ['is_passing']

if 'StaffLeavesPolicyRule' in globals():
    @admin.register(StaffLeavesPolicyRule)
    class StaffLeavesPolicyRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'rule_code', 'rule_name', 'threshold_value', 'is_enforced']
        list_filter = ['is_enforced']

if 'StaffLeavesSchedulePeriod' in globals():
    @admin.register(StaffLeavesSchedulePeriod)
    class StaffLeavesSchedulePeriodAdmin(admin.ModelAdmin):
        list_display = ['master', 'period_title', 'day_of_week', 'start_time', 'end_time', 'room_number']
        list_filter = ['day_of_week', 'is_break_period']

if 'StaffLeavesFeedbackReview' in globals():
    @admin.register(StaffLeavesFeedbackReview)
    class StaffLeavesFeedbackReviewAdmin(admin.ModelAdmin):
        list_display = ['master', 'reviewer_name', 'reviewer_role', 'rating', 'is_resolved', 'submitted_at']
        list_filter = ['rating', 'is_resolved']

if 'StaffLeavesWorkflowTransition' in globals():
    @admin.register(StaffLeavesWorkflowTransition)
    class StaffLeavesWorkflowTransitionAdmin(admin.ModelAdmin):
        list_display = ['master', 'from_stage', 'to_stage', 'actor_username', 'is_approved', 'transition_timestamp']
        list_filter = ['is_approved']

if 'StaffLeavesAccessRule' in globals():
    @admin.register(StaffLeavesAccessRule)
    class StaffLeavesAccessRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'role_allowed', 'can_read', 'can_write', 'can_delete', 'can_export']
        list_filter = ['role_allowed']

if 'StaffLeavesConfigurationParameter' in globals():
    @admin.register(StaffLeavesConfigurationParameter)
    class StaffLeavesConfigurationParameterAdmin(admin.ModelAdmin):
        list_display = ['master', 'param_key', 'param_value', 'data_type', 'is_editable']

if 'StaffLeavesDocumentAttachment' in globals():
    @admin.register(StaffLeavesDocumentAttachment)
    class StaffLeavesDocumentAttachmentAdmin(admin.ModelAdmin):
        list_display = ['master', 'title', 'mime_type', 'file_size_bytes', 'uploaded_by', 'uploaded_at']

if 'StaffLeavesAuditTrail' in globals():
    @admin.register(StaffLeavesAuditTrail)
    class StaffLeavesAuditTrailAdmin(admin.ModelAdmin):
        list_display = ['master', 'action_type', 'performed_by', 'timestamp']
        list_filter = ['action_type', 'timestamp']
        readonly_fields = ['master', 'action_type', 'performed_by', 'previous_state', 'new_state', 'timestamp', 'change_summary']

"""Django Admin configuration for EduFlow Chart of Accounts & Financial Ledger (ChartOfAccounts)."""
from django.contrib import admin
try:
    from .models import (
        ChartOfAccountsMaster, ChartOfAccountsItem, ChartOfAccountsAllocation,
        ChartOfAccountsMetricRecord, ChartOfAccountsPolicyRule, ChartOfAccountsSchedulePeriod,
        ChartOfAccountsFeedbackReview, ChartOfAccountsWorkflowTransition, ChartOfAccountsAccessRule,
        ChartOfAccountsConfigurationParameter, ChartOfAccountsDocumentAttachment, ChartOfAccountsAuditTrail
    )
except ImportError:
    try:
        from .models import (
            ChartOfAccountsMaster, ChartOfAccountsItem, ChartOfAccountsAllocation,
            ChartOfAccountsMetricRecord, ChartOfAccountsPolicyRule, ChartOfAccountsSchedulePeriod,
            ChartOfAccountsFeedbackReview, ChartOfAccountsWorkflowTransition, ChartOfAccountsAccessRule,
            ChartOfAccountsConfigurationParameter, ChartOfAccountsDocumentAttachment, ChartOfAccountsAuditTrail
        )
    except ImportError:
        pass

if 'ChartOfAccountsMaster' in globals():
    @admin.register(ChartOfAccountsMaster)
    class ChartOfAccountsMasterAdmin(admin.ModelAdmin):
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

if 'ChartOfAccountsItem' in globals():
    @admin.register(ChartOfAccountsItem)
    class ChartOfAccountsItemAdmin(admin.ModelAdmin):
        list_display = ['master', 'item_code', 'title', 'quantity', 'unit_rate', 'total_amount', 'is_completed']
        list_filter = ['is_completed', 'is_mandatory']
        search_fields = ['item_code', 'title']

if 'ChartOfAccountsAllocation' in globals():
    @admin.register(ChartOfAccountsAllocation)
    class ChartOfAccountsAllocationAdmin(admin.ModelAdmin):
        list_display = ['master', 'assignee_name', 'allocation_role', 'start_time', 'end_time', 'is_active']
        list_filter = ['is_active', 'allocation_role']
        search_fields = ['assignee_name', 'authorization_code']

if 'ChartOfAccountsMetricRecord' in globals():
    @admin.register(ChartOfAccountsMetricRecord)
    class ChartOfAccountsMetricRecordAdmin(admin.ModelAdmin):
        list_display = ['master', 'metric_name', 'target_value', 'actual_value', 'score_percentage', 'is_passing']
        list_filter = ['is_passing']

if 'ChartOfAccountsPolicyRule' in globals():
    @admin.register(ChartOfAccountsPolicyRule)
    class ChartOfAccountsPolicyRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'rule_code', 'rule_name', 'threshold_value', 'is_enforced']
        list_filter = ['is_enforced']

if 'ChartOfAccountsSchedulePeriod' in globals():
    @admin.register(ChartOfAccountsSchedulePeriod)
    class ChartOfAccountsSchedulePeriodAdmin(admin.ModelAdmin):
        list_display = ['master', 'period_title', 'day_of_week', 'start_time', 'end_time', 'room_number']
        list_filter = ['day_of_week', 'is_break_period']

if 'ChartOfAccountsFeedbackReview' in globals():
    @admin.register(ChartOfAccountsFeedbackReview)
    class ChartOfAccountsFeedbackReviewAdmin(admin.ModelAdmin):
        list_display = ['master', 'reviewer_name', 'reviewer_role', 'rating', 'is_resolved', 'submitted_at']
        list_filter = ['rating', 'is_resolved']

if 'ChartOfAccountsWorkflowTransition' in globals():
    @admin.register(ChartOfAccountsWorkflowTransition)
    class ChartOfAccountsWorkflowTransitionAdmin(admin.ModelAdmin):
        list_display = ['master', 'from_stage', 'to_stage', 'actor_username', 'is_approved', 'transition_timestamp']
        list_filter = ['is_approved']

if 'ChartOfAccountsAccessRule' in globals():
    @admin.register(ChartOfAccountsAccessRule)
    class ChartOfAccountsAccessRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'role_allowed', 'can_read', 'can_write', 'can_delete', 'can_export']
        list_filter = ['role_allowed']

if 'ChartOfAccountsConfigurationParameter' in globals():
    @admin.register(ChartOfAccountsConfigurationParameter)
    class ChartOfAccountsConfigurationParameterAdmin(admin.ModelAdmin):
        list_display = ['master', 'param_key', 'param_value', 'data_type', 'is_editable']

if 'ChartOfAccountsDocumentAttachment' in globals():
    @admin.register(ChartOfAccountsDocumentAttachment)
    class ChartOfAccountsDocumentAttachmentAdmin(admin.ModelAdmin):
        list_display = ['master', 'title', 'mime_type', 'file_size_bytes', 'uploaded_by', 'uploaded_at']

if 'ChartOfAccountsAuditTrail' in globals():
    @admin.register(ChartOfAccountsAuditTrail)
    class ChartOfAccountsAuditTrailAdmin(admin.ModelAdmin):
        list_display = ['master', 'action_type', 'performed_by', 'timestamp']
        list_filter = ['action_type', 'timestamp']
        readonly_fields = ['master', 'action_type', 'performed_by', 'previous_state', 'new_state', 'timestamp', 'change_summary']

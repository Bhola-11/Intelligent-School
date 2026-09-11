"""Django Admin configuration for EduFlow Financial Statements & Cash Registers (FinancialReports)."""
from django.contrib import admin
try:
    from .models import (
        FinancialReportsMaster, FinancialReportsItem, FinancialReportsAllocation,
        FinancialReportsMetricRecord, FinancialReportsPolicyRule, FinancialReportsSchedulePeriod,
        FinancialReportsFeedbackReview, FinancialReportsWorkflowTransition, FinancialReportsAccessRule,
        FinancialReportsConfigurationParameter, FinancialReportsDocumentAttachment, FinancialReportsAuditTrail
    )
except ImportError:
    try:
        from .models_financialreports import (
            FinancialReportsMaster, FinancialReportsItem, FinancialReportsAllocation,
            FinancialReportsMetricRecord, FinancialReportsPolicyRule, FinancialReportsSchedulePeriod,
            FinancialReportsFeedbackReview, FinancialReportsWorkflowTransition, FinancialReportsAccessRule,
            FinancialReportsConfigurationParameter, FinancialReportsDocumentAttachment, FinancialReportsAuditTrail
        )
    except ImportError:
        pass

if 'FinancialReportsMaster' in globals():
    @admin.register(FinancialReportsMaster)
    class FinancialReportsMasterAdmin(admin.ModelAdmin):
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

if 'FinancialReportsItem' in globals():
    @admin.register(FinancialReportsItem)
    class FinancialReportsItemAdmin(admin.ModelAdmin):
        list_display = ['master', 'item_code', 'title', 'quantity', 'unit_rate', 'total_amount', 'is_completed']
        list_filter = ['is_completed', 'is_mandatory']
        search_fields = ['item_code', 'title']

if 'FinancialReportsAllocation' in globals():
    @admin.register(FinancialReportsAllocation)
    class FinancialReportsAllocationAdmin(admin.ModelAdmin):
        list_display = ['master', 'assignee_name', 'allocation_role', 'start_time', 'end_time', 'is_active']
        list_filter = ['is_active', 'allocation_role']
        search_fields = ['assignee_name', 'authorization_code']

if 'FinancialReportsMetricRecord' in globals():
    @admin.register(FinancialReportsMetricRecord)
    class FinancialReportsMetricRecordAdmin(admin.ModelAdmin):
        list_display = ['master', 'metric_name', 'target_value', 'actual_value', 'score_percentage', 'is_passing']
        list_filter = ['is_passing']

if 'FinancialReportsPolicyRule' in globals():
    @admin.register(FinancialReportsPolicyRule)
    class FinancialReportsPolicyRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'rule_code', 'rule_name', 'threshold_value', 'is_enforced']
        list_filter = ['is_enforced']

if 'FinancialReportsSchedulePeriod' in globals():
    @admin.register(FinancialReportsSchedulePeriod)
    class FinancialReportsSchedulePeriodAdmin(admin.ModelAdmin):
        list_display = ['master', 'period_title', 'day_of_week', 'start_time', 'end_time', 'room_number']
        list_filter = ['day_of_week', 'is_break_period']

if 'FinancialReportsFeedbackReview' in globals():
    @admin.register(FinancialReportsFeedbackReview)
    class FinancialReportsFeedbackReviewAdmin(admin.ModelAdmin):
        list_display = ['master', 'reviewer_name', 'reviewer_role', 'rating', 'is_resolved', 'submitted_at']
        list_filter = ['rating', 'is_resolved']

if 'FinancialReportsWorkflowTransition' in globals():
    @admin.register(FinancialReportsWorkflowTransition)
    class FinancialReportsWorkflowTransitionAdmin(admin.ModelAdmin):
        list_display = ['master', 'from_stage', 'to_stage', 'actor_username', 'is_approved', 'transition_timestamp']
        list_filter = ['is_approved']

if 'FinancialReportsAccessRule' in globals():
    @admin.register(FinancialReportsAccessRule)
    class FinancialReportsAccessRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'role_allowed', 'can_read', 'can_write', 'can_delete', 'can_export']
        list_filter = ['role_allowed']

if 'FinancialReportsConfigurationParameter' in globals():
    @admin.register(FinancialReportsConfigurationParameter)
    class FinancialReportsConfigurationParameterAdmin(admin.ModelAdmin):
        list_display = ['master', 'param_key', 'param_value', 'data_type', 'is_editable']

if 'FinancialReportsDocumentAttachment' in globals():
    @admin.register(FinancialReportsDocumentAttachment)
    class FinancialReportsDocumentAttachmentAdmin(admin.ModelAdmin):
        list_display = ['master', 'title', 'mime_type', 'file_size_bytes', 'uploaded_by', 'uploaded_at']

if 'FinancialReportsAuditTrail' in globals():
    @admin.register(FinancialReportsAuditTrail)
    class FinancialReportsAuditTrailAdmin(admin.ModelAdmin):
        list_display = ['master', 'action_type', 'performed_by', 'timestamp']
        list_filter = ['action_type', 'timestamp']
        readonly_fields = ['master', 'action_type', 'performed_by', 'previous_state', 'new_state', 'timestamp', 'change_summary']

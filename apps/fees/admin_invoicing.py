"""Django Admin configuration for EduFlow Student Fee Invoicing & Billing Engine (Invoicing)."""
from django.contrib import admin
try:
    from .models import (
        InvoicingMaster, InvoicingItem, InvoicingAllocation,
        InvoicingMetricRecord, InvoicingPolicyRule, InvoicingSchedulePeriod,
        InvoicingFeedbackReview, InvoicingWorkflowTransition, InvoicingAccessRule,
        InvoicingConfigurationParameter, InvoicingDocumentAttachment, InvoicingAuditTrail
    )
except ImportError:
    try:
        from .models_invoicing import (
            InvoicingMaster, InvoicingItem, InvoicingAllocation,
            InvoicingMetricRecord, InvoicingPolicyRule, InvoicingSchedulePeriod,
            InvoicingFeedbackReview, InvoicingWorkflowTransition, InvoicingAccessRule,
            InvoicingConfigurationParameter, InvoicingDocumentAttachment, InvoicingAuditTrail
        )
    except ImportError:
        pass

if 'InvoicingMaster' in globals():
    @admin.register(InvoicingMaster)
    class InvoicingMasterAdmin(admin.ModelAdmin):
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

if 'InvoicingItem' in globals():
    @admin.register(InvoicingItem)
    class InvoicingItemAdmin(admin.ModelAdmin):
        list_display = ['master', 'item_code', 'title', 'quantity', 'unit_rate', 'total_amount', 'is_completed']
        list_filter = ['is_completed', 'is_mandatory']
        search_fields = ['item_code', 'title']

if 'InvoicingAllocation' in globals():
    @admin.register(InvoicingAllocation)
    class InvoicingAllocationAdmin(admin.ModelAdmin):
        list_display = ['master', 'assignee_name', 'allocation_role', 'start_time', 'end_time', 'is_active']
        list_filter = ['is_active', 'allocation_role']
        search_fields = ['assignee_name', 'authorization_code']

if 'InvoicingMetricRecord' in globals():
    @admin.register(InvoicingMetricRecord)
    class InvoicingMetricRecordAdmin(admin.ModelAdmin):
        list_display = ['master', 'metric_name', 'target_value', 'actual_value', 'score_percentage', 'is_passing']
        list_filter = ['is_passing']

if 'InvoicingPolicyRule' in globals():
    @admin.register(InvoicingPolicyRule)
    class InvoicingPolicyRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'rule_code', 'rule_name', 'threshold_value', 'is_enforced']
        list_filter = ['is_enforced']

if 'InvoicingSchedulePeriod' in globals():
    @admin.register(InvoicingSchedulePeriod)
    class InvoicingSchedulePeriodAdmin(admin.ModelAdmin):
        list_display = ['master', 'period_title', 'day_of_week', 'start_time', 'end_time', 'room_number']
        list_filter = ['day_of_week', 'is_break_period']

if 'InvoicingFeedbackReview' in globals():
    @admin.register(InvoicingFeedbackReview)
    class InvoicingFeedbackReviewAdmin(admin.ModelAdmin):
        list_display = ['master', 'reviewer_name', 'reviewer_role', 'rating', 'is_resolved', 'submitted_at']
        list_filter = ['rating', 'is_resolved']

if 'InvoicingWorkflowTransition' in globals():
    @admin.register(InvoicingWorkflowTransition)
    class InvoicingWorkflowTransitionAdmin(admin.ModelAdmin):
        list_display = ['master', 'from_stage', 'to_stage', 'actor_username', 'is_approved', 'transition_timestamp']
        list_filter = ['is_approved']

if 'InvoicingAccessRule' in globals():
    @admin.register(InvoicingAccessRule)
    class InvoicingAccessRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'role_allowed', 'can_read', 'can_write', 'can_delete', 'can_export']
        list_filter = ['role_allowed']

if 'InvoicingConfigurationParameter' in globals():
    @admin.register(InvoicingConfigurationParameter)
    class InvoicingConfigurationParameterAdmin(admin.ModelAdmin):
        list_display = ['master', 'param_key', 'param_value', 'data_type', 'is_editable']

if 'InvoicingDocumentAttachment' in globals():
    @admin.register(InvoicingDocumentAttachment)
    class InvoicingDocumentAttachmentAdmin(admin.ModelAdmin):
        list_display = ['master', 'title', 'mime_type', 'file_size_bytes', 'uploaded_by', 'uploaded_at']

if 'InvoicingAuditTrail' in globals():
    @admin.register(InvoicingAuditTrail)
    class InvoicingAuditTrailAdmin(admin.ModelAdmin):
        list_display = ['master', 'action_type', 'performed_by', 'timestamp']
        list_filter = ['action_type', 'timestamp']
        readonly_fields = ['master', 'action_type', 'performed_by', 'previous_state', 'new_state', 'timestamp', 'change_summary']

"""Django Admin configuration for EduFlow Inventory Categories & Asset Registry (AssetRegistry)."""
from django.contrib import admin
try:
    from .models import (
        AssetRegistryMaster, AssetRegistryItem, AssetRegistryAllocation,
        AssetRegistryMetricRecord, AssetRegistryPolicyRule, AssetRegistrySchedulePeriod,
        AssetRegistryFeedbackReview, AssetRegistryWorkflowTransition, AssetRegistryAccessRule,
        AssetRegistryConfigurationParameter, AssetRegistryDocumentAttachment, AssetRegistryAuditTrail
    )
except ImportError:
    try:
        from .models import (
            AssetRegistryMaster, AssetRegistryItem, AssetRegistryAllocation,
            AssetRegistryMetricRecord, AssetRegistryPolicyRule, AssetRegistrySchedulePeriod,
            AssetRegistryFeedbackReview, AssetRegistryWorkflowTransition, AssetRegistryAccessRule,
            AssetRegistryConfigurationParameter, AssetRegistryDocumentAttachment, AssetRegistryAuditTrail
        )
    except ImportError:
        pass

if 'AssetRegistryMaster' in globals():
    @admin.register(AssetRegistryMaster)
    class AssetRegistryMasterAdmin(admin.ModelAdmin):
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

if 'AssetRegistryItem' in globals():
    @admin.register(AssetRegistryItem)
    class AssetRegistryItemAdmin(admin.ModelAdmin):
        list_display = ['master', 'item_code', 'title', 'quantity', 'unit_rate', 'total_amount', 'is_completed']
        list_filter = ['is_completed', 'is_mandatory']
        search_fields = ['item_code', 'title']

if 'AssetRegistryAllocation' in globals():
    @admin.register(AssetRegistryAllocation)
    class AssetRegistryAllocationAdmin(admin.ModelAdmin):
        list_display = ['master', 'assignee_name', 'allocation_role', 'start_time', 'end_time', 'is_active']
        list_filter = ['is_active', 'allocation_role']
        search_fields = ['assignee_name', 'authorization_code']

if 'AssetRegistryMetricRecord' in globals():
    @admin.register(AssetRegistryMetricRecord)
    class AssetRegistryMetricRecordAdmin(admin.ModelAdmin):
        list_display = ['master', 'metric_name', 'target_value', 'actual_value', 'score_percentage', 'is_passing']
        list_filter = ['is_passing']

if 'AssetRegistryPolicyRule' in globals():
    @admin.register(AssetRegistryPolicyRule)
    class AssetRegistryPolicyRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'rule_code', 'rule_name', 'threshold_value', 'is_enforced']
        list_filter = ['is_enforced']

if 'AssetRegistrySchedulePeriod' in globals():
    @admin.register(AssetRegistrySchedulePeriod)
    class AssetRegistrySchedulePeriodAdmin(admin.ModelAdmin):
        list_display = ['master', 'period_title', 'day_of_week', 'start_time', 'end_time', 'room_number']
        list_filter = ['day_of_week', 'is_break_period']

if 'AssetRegistryFeedbackReview' in globals():
    @admin.register(AssetRegistryFeedbackReview)
    class AssetRegistryFeedbackReviewAdmin(admin.ModelAdmin):
        list_display = ['master', 'reviewer_name', 'reviewer_role', 'rating', 'is_resolved', 'submitted_at']
        list_filter = ['rating', 'is_resolved']

if 'AssetRegistryWorkflowTransition' in globals():
    @admin.register(AssetRegistryWorkflowTransition)
    class AssetRegistryWorkflowTransitionAdmin(admin.ModelAdmin):
        list_display = ['master', 'from_stage', 'to_stage', 'actor_username', 'is_approved', 'transition_timestamp']
        list_filter = ['is_approved']

if 'AssetRegistryAccessRule' in globals():
    @admin.register(AssetRegistryAccessRule)
    class AssetRegistryAccessRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'role_allowed', 'can_read', 'can_write', 'can_delete', 'can_export']
        list_filter = ['role_allowed']

if 'AssetRegistryConfigurationParameter' in globals():
    @admin.register(AssetRegistryConfigurationParameter)
    class AssetRegistryConfigurationParameterAdmin(admin.ModelAdmin):
        list_display = ['master', 'param_key', 'param_value', 'data_type', 'is_editable']

if 'AssetRegistryDocumentAttachment' in globals():
    @admin.register(AssetRegistryDocumentAttachment)
    class AssetRegistryDocumentAttachmentAdmin(admin.ModelAdmin):
        list_display = ['master', 'title', 'mime_type', 'file_size_bytes', 'uploaded_by', 'uploaded_at']

if 'AssetRegistryAuditTrail' in globals():
    @admin.register(AssetRegistryAuditTrail)
    class AssetRegistryAuditTrailAdmin(admin.ModelAdmin):
        list_display = ['master', 'action_type', 'performed_by', 'timestamp']
        list_filter = ['action_type', 'timestamp']
        readonly_fields = ['master', 'action_type', 'performed_by', 'previous_state', 'new_state', 'timestamp', 'change_summary']

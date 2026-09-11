"""Django Admin configuration for EduFlow Fee Categories & Structure Configuration (FeeStructures)."""
from django.contrib import admin
try:
    from .models import (
        FeeStructuresMaster, FeeStructuresItem, FeeStructuresAllocation,
        FeeStructuresMetricRecord, FeeStructuresPolicyRule, FeeStructuresSchedulePeriod,
        FeeStructuresFeedbackReview, FeeStructuresWorkflowTransition, FeeStructuresAccessRule,
        FeeStructuresConfigurationParameter, FeeStructuresDocumentAttachment, FeeStructuresAuditTrail
    )
except ImportError:
    try:
        from .models import (
            FeeStructuresMaster, FeeStructuresItem, FeeStructuresAllocation,
            FeeStructuresMetricRecord, FeeStructuresPolicyRule, FeeStructuresSchedulePeriod,
            FeeStructuresFeedbackReview, FeeStructuresWorkflowTransition, FeeStructuresAccessRule,
            FeeStructuresConfigurationParameter, FeeStructuresDocumentAttachment, FeeStructuresAuditTrail
        )
    except ImportError:
        pass

if 'FeeStructuresMaster' in globals():
    @admin.register(FeeStructuresMaster)
    class FeeStructuresMasterAdmin(admin.ModelAdmin):
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

if 'FeeStructuresItem' in globals():
    @admin.register(FeeStructuresItem)
    class FeeStructuresItemAdmin(admin.ModelAdmin):
        list_display = ['master', 'item_code', 'title', 'quantity', 'unit_rate', 'total_amount', 'is_completed']
        list_filter = ['is_completed', 'is_mandatory']
        search_fields = ['item_code', 'title']

if 'FeeStructuresAllocation' in globals():
    @admin.register(FeeStructuresAllocation)
    class FeeStructuresAllocationAdmin(admin.ModelAdmin):
        list_display = ['master', 'assignee_name', 'allocation_role', 'start_time', 'end_time', 'is_active']
        list_filter = ['is_active', 'allocation_role']
        search_fields = ['assignee_name', 'authorization_code']

if 'FeeStructuresMetricRecord' in globals():
    @admin.register(FeeStructuresMetricRecord)
    class FeeStructuresMetricRecordAdmin(admin.ModelAdmin):
        list_display = ['master', 'metric_name', 'target_value', 'actual_value', 'score_percentage', 'is_passing']
        list_filter = ['is_passing']

if 'FeeStructuresPolicyRule' in globals():
    @admin.register(FeeStructuresPolicyRule)
    class FeeStructuresPolicyRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'rule_code', 'rule_name', 'threshold_value', 'is_enforced']
        list_filter = ['is_enforced']

if 'FeeStructuresSchedulePeriod' in globals():
    @admin.register(FeeStructuresSchedulePeriod)
    class FeeStructuresSchedulePeriodAdmin(admin.ModelAdmin):
        list_display = ['master', 'period_title', 'day_of_week', 'start_time', 'end_time', 'room_number']
        list_filter = ['day_of_week', 'is_break_period']

if 'FeeStructuresFeedbackReview' in globals():
    @admin.register(FeeStructuresFeedbackReview)
    class FeeStructuresFeedbackReviewAdmin(admin.ModelAdmin):
        list_display = ['master', 'reviewer_name', 'reviewer_role', 'rating', 'is_resolved', 'submitted_at']
        list_filter = ['rating', 'is_resolved']

if 'FeeStructuresWorkflowTransition' in globals():
    @admin.register(FeeStructuresWorkflowTransition)
    class FeeStructuresWorkflowTransitionAdmin(admin.ModelAdmin):
        list_display = ['master', 'from_stage', 'to_stage', 'actor_username', 'is_approved', 'transition_timestamp']
        list_filter = ['is_approved']

if 'FeeStructuresAccessRule' in globals():
    @admin.register(FeeStructuresAccessRule)
    class FeeStructuresAccessRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'role_allowed', 'can_read', 'can_write', 'can_delete', 'can_export']
        list_filter = ['role_allowed']

if 'FeeStructuresConfigurationParameter' in globals():
    @admin.register(FeeStructuresConfigurationParameter)
    class FeeStructuresConfigurationParameterAdmin(admin.ModelAdmin):
        list_display = ['master', 'param_key', 'param_value', 'data_type', 'is_editable']

if 'FeeStructuresDocumentAttachment' in globals():
    @admin.register(FeeStructuresDocumentAttachment)
    class FeeStructuresDocumentAttachmentAdmin(admin.ModelAdmin):
        list_display = ['master', 'title', 'mime_type', 'file_size_bytes', 'uploaded_by', 'uploaded_at']

if 'FeeStructuresAuditTrail' in globals():
    @admin.register(FeeStructuresAuditTrail)
    class FeeStructuresAuditTrailAdmin(admin.ModelAdmin):
        list_display = ['master', 'action_type', 'performed_by', 'timestamp']
        list_filter = ['action_type', 'timestamp']
        readonly_fields = ['master', 'action_type', 'performed_by', 'previous_state', 'new_state', 'timestamp', 'change_summary']

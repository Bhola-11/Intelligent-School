"""Django Admin configuration for EduFlow Student Document Vault & Verifications (Documents)."""
from django.contrib import admin
try:
    from .models import (
        DocumentsMaster, DocumentsItem, DocumentsAllocation,
        DocumentsMetricRecord, DocumentsPolicyRule, DocumentsSchedulePeriod,
        DocumentsFeedbackReview, DocumentsWorkflowTransition, DocumentsAccessRule,
        DocumentsConfigurationParameter, DocumentsDocumentAttachment, DocumentsAuditTrail
    )
except ImportError:
    try:
        from .models_documents import (
            DocumentsMaster, DocumentsItem, DocumentsAllocation,
            DocumentsMetricRecord, DocumentsPolicyRule, DocumentsSchedulePeriod,
            DocumentsFeedbackReview, DocumentsWorkflowTransition, DocumentsAccessRule,
            DocumentsConfigurationParameter, DocumentsDocumentAttachment, DocumentsAuditTrail
        )
    except ImportError:
        pass

if 'DocumentsMaster' in globals():
    @admin.register(DocumentsMaster)
    class DocumentsMasterAdmin(admin.ModelAdmin):
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

if 'DocumentsItem' in globals():
    @admin.register(DocumentsItem)
    class DocumentsItemAdmin(admin.ModelAdmin):
        list_display = ['master', 'item_code', 'title', 'quantity', 'unit_rate', 'total_amount', 'is_completed']
        list_filter = ['is_completed', 'is_mandatory']
        search_fields = ['item_code', 'title']

if 'DocumentsAllocation' in globals():
    @admin.register(DocumentsAllocation)
    class DocumentsAllocationAdmin(admin.ModelAdmin):
        list_display = ['master', 'assignee_name', 'allocation_role', 'start_time', 'end_time', 'is_active']
        list_filter = ['is_active', 'allocation_role']
        search_fields = ['assignee_name', 'authorization_code']

if 'DocumentsMetricRecord' in globals():
    @admin.register(DocumentsMetricRecord)
    class DocumentsMetricRecordAdmin(admin.ModelAdmin):
        list_display = ['master', 'metric_name', 'target_value', 'actual_value', 'score_percentage', 'is_passing']
        list_filter = ['is_passing']

if 'DocumentsPolicyRule' in globals():
    @admin.register(DocumentsPolicyRule)
    class DocumentsPolicyRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'rule_code', 'rule_name', 'threshold_value', 'is_enforced']
        list_filter = ['is_enforced']

if 'DocumentsSchedulePeriod' in globals():
    @admin.register(DocumentsSchedulePeriod)
    class DocumentsSchedulePeriodAdmin(admin.ModelAdmin):
        list_display = ['master', 'period_title', 'day_of_week', 'start_time', 'end_time', 'room_number']
        list_filter = ['day_of_week', 'is_break_period']

if 'DocumentsFeedbackReview' in globals():
    @admin.register(DocumentsFeedbackReview)
    class DocumentsFeedbackReviewAdmin(admin.ModelAdmin):
        list_display = ['master', 'reviewer_name', 'reviewer_role', 'rating', 'is_resolved', 'submitted_at']
        list_filter = ['rating', 'is_resolved']

if 'DocumentsWorkflowTransition' in globals():
    @admin.register(DocumentsWorkflowTransition)
    class DocumentsWorkflowTransitionAdmin(admin.ModelAdmin):
        list_display = ['master', 'from_stage', 'to_stage', 'actor_username', 'is_approved', 'transition_timestamp']
        list_filter = ['is_approved']

if 'DocumentsAccessRule' in globals():
    @admin.register(DocumentsAccessRule)
    class DocumentsAccessRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'role_allowed', 'can_read', 'can_write', 'can_delete', 'can_export']
        list_filter = ['role_allowed']

if 'DocumentsConfigurationParameter' in globals():
    @admin.register(DocumentsConfigurationParameter)
    class DocumentsConfigurationParameterAdmin(admin.ModelAdmin):
        list_display = ['master', 'param_key', 'param_value', 'data_type', 'is_editable']

if 'DocumentsDocumentAttachment' in globals():
    @admin.register(DocumentsDocumentAttachment)
    class DocumentsDocumentAttachmentAdmin(admin.ModelAdmin):
        list_display = ['master', 'title', 'mime_type', 'file_size_bytes', 'uploaded_by', 'uploaded_at']

if 'DocumentsAuditTrail' in globals():
    @admin.register(DocumentsAuditTrail)
    class DocumentsAuditTrailAdmin(admin.ModelAdmin):
        list_display = ['master', 'action_type', 'performed_by', 'timestamp']
        list_filter = ['action_type', 'timestamp']
        readonly_fields = ['master', 'action_type', 'performed_by', 'previous_state', 'new_state', 'timestamp', 'change_summary']

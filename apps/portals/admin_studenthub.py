"""Django Admin configuration for EduFlow Student Learning Hub & Portal (StudentHub)."""
from django.contrib import admin
try:
    from .models import (
        StudentHubMaster, StudentHubItem, StudentHubAllocation,
        StudentHubMetricRecord, StudentHubPolicyRule, StudentHubSchedulePeriod,
        StudentHubFeedbackReview, StudentHubWorkflowTransition, StudentHubAccessRule,
        StudentHubConfigurationParameter, StudentHubDocumentAttachment, StudentHubAuditTrail
    )
except ImportError:
    try:
        from .models_studenthub import (
            StudentHubMaster, StudentHubItem, StudentHubAllocation,
            StudentHubMetricRecord, StudentHubPolicyRule, StudentHubSchedulePeriod,
            StudentHubFeedbackReview, StudentHubWorkflowTransition, StudentHubAccessRule,
            StudentHubConfigurationParameter, StudentHubDocumentAttachment, StudentHubAuditTrail
        )
    except ImportError:
        pass

if 'StudentHubMaster' in globals():
    @admin.register(StudentHubMaster)
    class StudentHubMasterAdmin(admin.ModelAdmin):
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

if 'StudentHubItem' in globals():
    @admin.register(StudentHubItem)
    class StudentHubItemAdmin(admin.ModelAdmin):
        list_display = ['master', 'item_code', 'title', 'quantity', 'unit_rate', 'total_amount', 'is_completed']
        list_filter = ['is_completed', 'is_mandatory']
        search_fields = ['item_code', 'title']

if 'StudentHubAllocation' in globals():
    @admin.register(StudentHubAllocation)
    class StudentHubAllocationAdmin(admin.ModelAdmin):
        list_display = ['master', 'assignee_name', 'allocation_role', 'start_time', 'end_time', 'is_active']
        list_filter = ['is_active', 'allocation_role']
        search_fields = ['assignee_name', 'authorization_code']

if 'StudentHubMetricRecord' in globals():
    @admin.register(StudentHubMetricRecord)
    class StudentHubMetricRecordAdmin(admin.ModelAdmin):
        list_display = ['master', 'metric_name', 'target_value', 'actual_value', 'score_percentage', 'is_passing']
        list_filter = ['is_passing']

if 'StudentHubPolicyRule' in globals():
    @admin.register(StudentHubPolicyRule)
    class StudentHubPolicyRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'rule_code', 'rule_name', 'threshold_value', 'is_enforced']
        list_filter = ['is_enforced']

if 'StudentHubSchedulePeriod' in globals():
    @admin.register(StudentHubSchedulePeriod)
    class StudentHubSchedulePeriodAdmin(admin.ModelAdmin):
        list_display = ['master', 'period_title', 'day_of_week', 'start_time', 'end_time', 'room_number']
        list_filter = ['day_of_week', 'is_break_period']

if 'StudentHubFeedbackReview' in globals():
    @admin.register(StudentHubFeedbackReview)
    class StudentHubFeedbackReviewAdmin(admin.ModelAdmin):
        list_display = ['master', 'reviewer_name', 'reviewer_role', 'rating', 'is_resolved', 'submitted_at']
        list_filter = ['rating', 'is_resolved']

if 'StudentHubWorkflowTransition' in globals():
    @admin.register(StudentHubWorkflowTransition)
    class StudentHubWorkflowTransitionAdmin(admin.ModelAdmin):
        list_display = ['master', 'from_stage', 'to_stage', 'actor_username', 'is_approved', 'transition_timestamp']
        list_filter = ['is_approved']

if 'StudentHubAccessRule' in globals():
    @admin.register(StudentHubAccessRule)
    class StudentHubAccessRuleAdmin(admin.ModelAdmin):
        list_display = ['master', 'role_allowed', 'can_read', 'can_write', 'can_delete', 'can_export']
        list_filter = ['role_allowed']

if 'StudentHubConfigurationParameter' in globals():
    @admin.register(StudentHubConfigurationParameter)
    class StudentHubConfigurationParameterAdmin(admin.ModelAdmin):
        list_display = ['master', 'param_key', 'param_value', 'data_type', 'is_editable']

if 'StudentHubDocumentAttachment' in globals():
    @admin.register(StudentHubDocumentAttachment)
    class StudentHubDocumentAttachmentAdmin(admin.ModelAdmin):
        list_display = ['master', 'title', 'mime_type', 'file_size_bytes', 'uploaded_by', 'uploaded_at']

if 'StudentHubAuditTrail' in globals():
    @admin.register(StudentHubAuditTrail)
    class StudentHubAuditTrailAdmin(admin.ModelAdmin):
        list_display = ['master', 'action_type', 'performed_by', 'timestamp']
        list_filter = ['action_type', 'timestamp']
        readonly_fields = ['master', 'action_type', 'performed_by', 'previous_state', 'new_state', 'timestamp', 'change_summary']

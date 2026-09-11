"""
Forms for EduFlow Institutional KPI & Executive Metrics (InstitutionKPI).
ModelForms and validation logic for all 12 domain entities.
"""

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
try:
    from .models import (
        InstitutionKPIMaster, InstitutionKPIItem, InstitutionKPIAllocation,
        InstitutionKPIMetricRecord, InstitutionKPIPolicyRule, InstitutionKPISchedulePeriod,
        InstitutionKPIFeedbackReview, InstitutionKPIWorkflowTransition, InstitutionKPIAccessRule,
        InstitutionKPIConfigurationParameter, InstitutionKPIDocumentAttachment, InstitutionKPIAuditTrail
    )
except ImportError:
    try:
        from .models_institutionkpi import (
            InstitutionKPIMaster, InstitutionKPIItem, InstitutionKPIAllocation,
            InstitutionKPIMetricRecord, InstitutionKPIPolicyRule, InstitutionKPISchedulePeriod,
            InstitutionKPIFeedbackReview, InstitutionKPIWorkflowTransition, InstitutionKPIAccessRule,
            InstitutionKPIConfigurationParameter, InstitutionKPIDocumentAttachment, InstitutionKPIAuditTrail
        )
    except ImportError:
        pass

class InstitutionKPIMasterForm(forms.ModelForm):
    """Primary form for creating and updating InstitutionKPI master records."""
    class Meta:
        try:
            model = InstitutionKPIMaster
            fields = [
                'code', 'name', 'short_name', 'category', 'tier', 'scope', 'priority', 'status',
                'capacity', 'current_occupancy', 'reserved_headroom', 'weightage', 'budget_allocated', 'cost_incurred',
                'effective_start_date', 'effective_end_date', 'is_recurring', 'is_public', 'is_locked', 'requires_director_approval',
                'description', 'operational_guidelines', 'internal_notes', 'tags'
            ]
            widgets = {
                'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. INST-001'}),
                'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Official Title'}),
                'short_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Display Short Name'}),
                'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category'}),
                'tier': forms.Select(attrs={'class': 'form-select'}),
                'scope': forms.Select(attrs={'class': 'form-select'}),
                'priority': forms.Select(attrs={'class': 'form-select'}),
                'status': forms.Select(attrs={'class': 'form-select'}),
                'capacity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
                'current_occupancy': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
                'reserved_headroom': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
                'weightage': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
                'budget_allocated': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
                'cost_incurred': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
                'effective_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                'effective_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
                'operational_guidelines': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                'internal_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'comma, separated, tags'}),
                'is_recurring': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'is_locked': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'requires_director_approval': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            }
        except NameError:
            fields = '__all__'

    def clean_code(self):
        code = self.cleaned_data.get('code', '').strip().upper()
        if len(code) < 3:
            raise ValidationError(_("Code identifier must contain at least 3 characters."))
        return code

    def clean_capacity(self):
        cap = self.cleaned_data.get('capacity', 0)
        if cap <= 0:
            raise ValidationError(_("Capacity must be strictly positive."))
        return cap

    def clean_budget_allocated(self):
        budget = self.cleaned_data.get('budget_allocated', 0)
        if budget < 0:
            raise ValidationError(_("Allocated budget cannot be negative."))
        return budget

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('effective_start_date')
        end = cleaned_data.get('effective_end_date')
        if start and end and end < start:
            self.add_error('effective_end_date', _("End date cannot precede the start date."))
        return cleaned_data


class InstitutionKPIItemForm(forms.ModelForm):
    """Form for sub-items and component line-items."""
    class Meta:
        try:
            model = InstitutionKPIItem
            fields = ['item_code', 'title', 'sequence_order', 'unit_measure', 'quantity', 'unit_rate', 'is_mandatory', 'remarks']
            widgets = {
                'item_code': forms.TextInput(attrs={'class': 'form-control'}),
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'sequence_order': forms.NumberInput(attrs={'class': 'form-control'}),
                'unit_measure': forms.TextInput(attrs={'class': 'form-control'}),
                'quantity': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
                'unit_rate': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
                'is_mandatory': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            }
        except NameError:
            fields = '__all__'

    def clean_item_code(self):
        code = self.cleaned_data.get('item_code', '').strip().upper()
        if not code:
            raise ValidationError(_("Item code is mandatory."))
        return code


class InstitutionKPIAllocationForm(forms.ModelForm):
    """Form for resource and faculty allocations."""
    class Meta:
        try:
            model = InstitutionKPIAllocation
            fields = ['assignee_id', 'assignee_name', 'allocation_role', 'start_time', 'end_time', 'allocated_quota', 'is_active', 'authorization_code', 'notes']
            widgets = {
                'assignee_id': forms.NumberInput(attrs={'class': 'form-control'}),
                'assignee_name': forms.TextInput(attrs={'class': 'form-control'}),
                'allocation_role': forms.TextInput(attrs={'class': 'form-control'}),
                'start_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
                'end_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
                'allocated_quota': forms.NumberInput(attrs={'class': 'form-control'}),
                'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'authorization_code': forms.TextInput(attrs={'class': 'form-control'}),
                'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            }
        except NameError:
            fields = '__all__'


class InstitutionKPIMetricRecordForm(forms.ModelForm):
    """Form for KPI metric observations."""
    class Meta:
        try:
            model = InstitutionKPIMetricRecord
            fields = ['metric_name', 'target_value', 'actual_value', 'evaluated_at', 'evaluator_remarks']
            widgets = {
                'metric_name': forms.TextInput(attrs={'class': 'form-control'}),
                'target_value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
                'actual_value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
                'evaluated_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
                'evaluator_remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            }
        except NameError:
            fields = '__all__'


class InstitutionKPIPolicyRuleForm(forms.ModelForm):
    """Form for institutional governance rules."""
    class Meta:
        try:
            model = InstitutionKPIPolicyRule
            fields = ['rule_code', 'rule_name', 'threshold_value', 'comparison_operator', 'action_on_breach', 'is_enforced', 'rule_description']
            widgets = {
                'rule_code': forms.TextInput(attrs={'class': 'form-control'}),
                'rule_name': forms.TextInput(attrs={'class': 'form-control'}),
                'threshold_value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
                'comparison_operator': forms.Select(attrs={'class': 'form-select'}, choices=[
                    ('GREATER_THAN_EQUAL', 'Greater than or Equal'),
                    ('LESS_THAN_EQUAL', 'Less than or Equal'),
                    ('EQUAL', 'Exact Match'),
                ]),
                'action_on_breach': forms.TextInput(attrs={'class': 'form-control'}),
                'is_enforced': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'rule_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            }
        except NameError:
            fields = '__all__'


class InstitutionKPISchedulePeriodForm(forms.ModelForm):
    """Form for timetable and schedule periods."""
    class Meta:
        try:
            model = InstitutionKPISchedulePeriod
            fields = ['period_title', 'day_of_week', 'start_time', 'end_time', 'is_break_period', 'room_number', 'session_notes']
            widgets = {
                'period_title': forms.TextInput(attrs={'class': 'form-control'}),
                'day_of_week': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 7}),
                'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
                'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
                'is_break_period': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'room_number': forms.TextInput(attrs={'class': 'form-control'}),
                'session_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            }
        except NameError:
            fields = '__all__'


class InstitutionKPIFeedbackReviewForm(forms.ModelForm):
    """Form for qualitative feedback and evaluation."""
    class Meta:
        try:
            model = InstitutionKPIFeedbackReview
            fields = ['reviewer_role', 'reviewer_name', 'rating', 'qualitative_feedback', 'actionable_recommendations', 'is_resolved']
            widgets = {
                'reviewer_role': forms.TextInput(attrs={'class': 'form-control'}),
                'reviewer_name': forms.TextInput(attrs={'class': 'form-control'}),
                'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
                'qualitative_feedback': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                'actionable_recommendations': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
                'is_resolved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            }
        except NameError:
            fields = '__all__'


class InstitutionKPIWorkflowTransitionForm(forms.ModelForm):
    """Form for submitting workflow approval transitions."""
    class Meta:
        try:
            model = InstitutionKPIWorkflowTransition
            fields = ['from_stage', 'to_stage', 'actor_username', 'approver_comments', 'is_approved']
            widgets = {
                'from_stage': forms.TextInput(attrs={'class': 'form-control'}),
                'to_stage': forms.TextInput(attrs={'class': 'form-control'}),
                'actor_username': forms.TextInput(attrs={'class': 'form-control'}),
                'approver_comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
                'is_approved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            }
        except NameError:
            fields = '__all__'


class InstitutionKPIAccessRuleForm(forms.ModelForm):
    """Form for object-level permission rules."""
    class Meta:
        try:
            model = InstitutionKPIAccessRule
            fields = ['role_allowed', 'can_read', 'can_write', 'can_delete', 'can_export']
            widgets = {
                'role_allowed': forms.TextInput(attrs={'class': 'form-control'}),
                'can_read': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'can_write': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'can_delete': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'can_export': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            }
        except NameError:
            fields = '__all__'


class InstitutionKPIConfigurationParameterForm(forms.ModelForm):
    """Form for key-value configuration parameters."""
    class Meta:
        try:
            model = InstitutionKPIConfigurationParameter
            fields = ['param_key', 'param_value', 'data_type', 'is_editable', 'description']
            widgets = {
                'param_key': forms.TextInput(attrs={'class': 'form-control'}),
                'param_value': forms.TextInput(attrs={'class': 'form-control'}),
                'data_type': forms.Select(attrs={'class': 'form-select'}, choices=[
                    ('STRING', 'String'), ('INTEGER', 'Integer'), ('BOOLEAN', 'Boolean'), ('JSON', 'JSON Document')
                ]),
                'is_editable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'description': forms.TextInput(attrs={'class': 'form-control'}),
            }
        except NameError:
            fields = '__all__'


class InstitutionKPIDocumentAttachmentForm(forms.ModelForm):
    """Form for registering official document attachments."""
    class Meta:
        try:
            model = InstitutionKPIDocumentAttachment
            fields = ['title', 'file_path', 'file_size_bytes', 'mime_type', 'checksum_hash']
            widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'file_path': forms.TextInput(attrs={'class': 'form-control'}),
                'file_size_bytes': forms.NumberInput(attrs={'class': 'form-control'}),
                'mime_type': forms.TextInput(attrs={'class': 'form-control'}),
                'checksum_hash': forms.TextInput(attrs={'class': 'form-control'}),
            }
        except NameError:
            fields = '__all__'


class InstitutionKPIFilterForm(forms.Form):
    """Filter toolbar for search, tier, status, priority, and date range."""
    q = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by code, title or tags...'}))
    category = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category'}))
    tier = forms.ChoiceField(
        required=False,
        choices=[('', 'All Tiers'), ('TIER_1', 'Tier 1 - Executive'), ('TIER_2', 'Tier 2 - Departmental'), ('TIER_3', 'Tier 3 - Unit'), ('TIER_4', 'Tier 4 - Support')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    status = forms.ChoiceField(
        required=False,
        choices=[('', 'All Statuses'), ('ACTIVE', 'Active'), ('PENDING_REVIEW', 'Pending Review'), ('APPROVED', 'Approved'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed'), ('ARCHIVED', 'Archived')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    priority = forms.ChoiceField(
        required=False,
        choices=[('', 'All Priorities'), ('LOW', 'Low'), ('NORMAL', 'Normal'), ('HIGH', 'High'), ('CRITICAL', 'Critical')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    date_from = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    date_to = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))


class InstitutionKPIBulkActionForm(forms.Form):
    """Bulk action handler for multi-record operations."""
    selected_ids = forms.CharField(widget=forms.HiddenInput())
    action = forms.ChoiceField(choices=[
        ('ACTIVATE', 'Mark as Active'),
        ('SUSPEND', 'Temporarily Suspend'),
        ('ARCHIVE', 'Archive Records'),
        ('DELETE', 'Delete Selected'),
    ], widget=forms.Select(attrs={'class': 'form-select'}))

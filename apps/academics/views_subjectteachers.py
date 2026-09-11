"""
Views for EduFlow Teacher-Class-Subject Allocation Matrix (SubjectTeachers).
Complete Class-Based Views and API endpoints for all 12 domain entities.
"""

import csv
import json
from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.db.models import Q, Avg, Sum, Count

try:
    from .models import (
        SubjectTeachersMaster, SubjectTeachersItem, SubjectTeachersAllocation,
        SubjectTeachersMetricRecord, SubjectTeachersPolicyRule, SubjectTeachersSchedulePeriod,
        SubjectTeachersFeedbackReview, SubjectTeachersWorkflowTransition, SubjectTeachersAccessRule,
        SubjectTeachersConfigurationParameter, SubjectTeachersDocumentAttachment, SubjectTeachersAuditTrail
    )
    from .forms import (
        SubjectTeachersMasterForm, SubjectTeachersItemForm, SubjectTeachersAllocationForm,
        SubjectTeachersMetricRecordForm, SubjectTeachersPolicyRuleForm, SubjectTeachersSchedulePeriodForm,
        SubjectTeachersFeedbackReviewForm, SubjectTeachersWorkflowTransitionForm, SubjectTeachersAccessRuleForm,
        SubjectTeachersConfigurationParameterForm, SubjectTeachersDocumentAttachmentForm, SubjectTeachersFilterForm,
        SubjectTeachersBulkActionForm
    )
except ImportError:
    try:
        from .models_subjectteachers import (
            SubjectTeachersMaster, SubjectTeachersItem, SubjectTeachersAllocation,
            SubjectTeachersMetricRecord, SubjectTeachersPolicyRule, SubjectTeachersSchedulePeriod,
            SubjectTeachersFeedbackReview, SubjectTeachersWorkflowTransition, SubjectTeachersAccessRule,
            SubjectTeachersConfigurationParameter, SubjectTeachersDocumentAttachment, SubjectTeachersAuditTrail
        )
        from .forms_subjectteachers import (
            SubjectTeachersMasterForm, SubjectTeachersItemForm, SubjectTeachersAllocationForm,
            SubjectTeachersMetricRecordForm, SubjectTeachersPolicyRuleForm, SubjectTeachersSchedulePeriodForm,
            SubjectTeachersFeedbackReviewForm, SubjectTeachersWorkflowTransitionForm, SubjectTeachersAccessRuleForm,
            SubjectTeachersConfigurationParameterForm, SubjectTeachersDocumentAttachmentForm, SubjectTeachersFilterForm,
            SubjectTeachersBulkActionForm
        )
    except ImportError:
        pass

# -----------------------------------------------------------------------------
# 1. Master Entity Views
# -----------------------------------------------------------------------------
class SubjectTeachersListView(LoginRequiredMixin, ListView):
    template_name = 'academics/subjectteachers_list.html'
    context_object_name = 'records'
    paginate_by = 25

    def get_queryset(self):
        qs = SubjectTeachersMaster.objects.all() if 'SubjectTeachersMaster' in globals() else []
        if not qs:
            return []
        q = self.request.GET.get('q')
        status = self.request.GET.get('status')
        priority = self.request.GET.get('priority')
        tier = self.request.GET.get('tier')
        category = self.request.GET.get('category')

        if q:
            qs = qs.filter(Q(name__icontains=q) | Q(code__icontains=q) | Q(tags__icontains=q))
        if status:
            qs = qs.filter(status=status)
        if priority:
            qs = qs.filter(priority=priority)
        if tier:
            qs = qs.filter(tier=tier)
        if category:
            qs = qs.filter(category__icontains=category)
        return qs.order_by('-created_at')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['filter_form'] = SubjectTeachersFilterForm(self.request.GET) if 'SubjectTeachersFilterForm' in globals() else None
        ctx['bulk_form'] = SubjectTeachersBulkActionForm() if 'SubjectTeachersBulkActionForm' in globals() else None
        ctx['total_count'] = SubjectTeachersMaster.objects.count() if 'SubjectTeachersMaster' in globals() else 0
        ctx['active_count'] = SubjectTeachersMaster.objects.filter(status='ACTIVE').count() if 'SubjectTeachersMaster' in globals() else 0
        ctx['pending_count'] = SubjectTeachersMaster.objects.filter(status='PENDING_REVIEW').count() if 'SubjectTeachersMaster' in globals() else 0
        ctx['page_title'] = "Teacher-Class-Subject Allocation Matrix Directory"
        ctx['domain_name'] = "SubjectTeachers"
        return ctx

class SubjectTeachersDetailView(LoginRequiredMixin, DetailView):
    template_name = 'academics/subjectteachers_detail.html'
    context_object_name = 'record'

    def get_object(self):
        return get_object_or_404(SubjectTeachersMaster, pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        obj = self.get_object()
        ctx['items'] = obj.items.all() if hasattr(obj, 'items') else []
        ctx['allocations'] = obj.allocations.all() if hasattr(obj, 'allocations') else []
        ctx['metrics'] = obj.metrics.all() if hasattr(obj, 'metrics') else []
        ctx['policy_rules'] = obj.policy_rules.all() if hasattr(obj, 'policy_rules') else []
        ctx['schedule_periods'] = obj.schedule_periods.all() if hasattr(obj, 'schedule_periods') else []
        ctx['reviews'] = obj.reviews.all() if hasattr(obj, 'reviews') else []
        ctx['workflow_transitions'] = obj.workflow_transitions.all() if hasattr(obj, 'workflow_transitions') else []
        ctx['access_rules'] = obj.access_rules.all() if hasattr(obj, 'access_rules') else []
        ctx['config_parameters'] = obj.config_parameters.all() if hasattr(obj, 'config_parameters') else []
        ctx['attachments'] = obj.attachments.all() if hasattr(obj, 'attachments') else []
        ctx['audit_records'] = obj.audit_records.all()[:25] if hasattr(obj, 'audit_records') else []
        return ctx

class SubjectTeachersCreateView(LoginRequiredMixin, CreateView):
    template_name = 'academics/subjectteachers_form.html'
    form_class = SubjectTeachersMasterForm
    success_url = reverse_lazy('academics:subjectteachers_list')

    def form_valid(self, form):
        form.instance.created_by_user = self.request.user.username
        form.instance.updated_by_user = self.request.user.username
        messages.success(self.request, f"SubjectTeachers record '{form.instance.name}' created successfully.")
        return super().form_valid(form)

class SubjectTeachersUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'academics/subjectteachers_form.html'
    form_class = SubjectTeachersMasterForm
    success_url = reverse_lazy('academics:subjectteachers_list')

    def get_object(self):
        return get_object_or_404(SubjectTeachersMaster, pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        form.instance.updated_by_user = self.request.user.username
        messages.success(self.request, f"SubjectTeachers record updated successfully.")
        return super().form_valid(form)

class SubjectTeachersDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'academics/subjectteachers_confirm_delete.html'
    success_url = reverse_lazy('academics:subjectteachers_list')

    def get_object(self):
        return get_object_or_404(SubjectTeachersMaster, pk=self.kwargs.get('pk'))

# -----------------------------------------------------------------------------
# 2. Line Item Views
# -----------------------------------------------------------------------------
class SubjectTeachersItemCreateView(LoginRequiredMixin, CreateView):
    form_class = SubjectTeachersItemForm
    template_name = 'academics/subjectteachers_form.html'

    def form_valid(self, form):
        master = get_object_or_404(SubjectTeachersMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, f"Added item '{form.instance.title}' to {master.name}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('academics:subjectteachers_detail', kwargs={'pk': self.kwargs.get('master_pk')})

class SubjectTeachersItemUpdateView(LoginRequiredMixin, UpdateView):
    form_class = SubjectTeachersItemForm
    template_name = 'academics/subjectteachers_form.html'

    def get_object(self):
        return get_object_or_404(SubjectTeachersItem, pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse('academics:subjectteachers_detail', kwargs={'pk': self.object.master_id})

class SubjectTeachersItemDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'academics/subjectteachers_confirm_delete.html'

    def get_object(self):
        return get_object_or_404(SubjectTeachersItem, pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse('academics:subjectteachers_detail', kwargs={'pk': self.object.master_id})

# -----------------------------------------------------------------------------
# 3. Allocation Views
# -----------------------------------------------------------------------------
class SubjectTeachersAllocationCreateView(LoginRequiredMixin, CreateView):
    form_class = SubjectTeachersAllocationForm
    template_name = 'academics/subjectteachers_form.html'

    def form_valid(self, form):
        master = get_object_or_404(SubjectTeachersMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, f"Allocated resource to {form.instance.assignee_name}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('academics:subjectteachers_detail', kwargs={'pk': self.kwargs.get('master_pk')})

class SubjectTeachersAllocationReleaseView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        alloc = get_object_or_404(SubjectTeachersAllocation, pk=self.kwargs.get('pk'))
        alloc.is_active = False
        alloc.end_time = timezone.now()
        alloc.save()
        messages.info(request, f"Allocation for {alloc.assignee_name} released.")
        return redirect('academics:subjectteachers_detail', pk=alloc.master_id)

# -----------------------------------------------------------------------------
# 4. Metric Record Views
# -----------------------------------------------------------------------------
class SubjectTeachersMetricCreateView(LoginRequiredMixin, CreateView):
    form_class = SubjectTeachersMetricRecordForm
    template_name = 'academics/subjectteachers_form.html'

    def form_valid(self, form):
        master = get_object_or_404(SubjectTeachersMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, f"Recorded metric {form.instance.metric_name}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('academics:subjectteachers_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 5. Policy Rule Views
# -----------------------------------------------------------------------------
class SubjectTeachersPolicyRuleCreateView(LoginRequiredMixin, CreateView):
    form_class = SubjectTeachersPolicyRuleForm
    template_name = 'academics/subjectteachers_form.html'

    def form_valid(self, form):
        master = get_object_or_404(SubjectTeachersMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, f"Configured policy rule {form.instance.rule_name}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('academics:subjectteachers_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 6. Schedule Period Views
# -----------------------------------------------------------------------------
class SubjectTeachersSchedulePeriodCreateView(LoginRequiredMixin, CreateView):
    form_class = SubjectTeachersSchedulePeriodForm
    template_name = 'academics/subjectteachers_form.html'

    def form_valid(self, form):
        master = get_object_or_404(SubjectTeachersMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, f"Added schedule period {form.instance.period_title}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('academics:subjectteachers_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 7. Feedback Review Views
# -----------------------------------------------------------------------------
class SubjectTeachersFeedbackReviewCreateView(LoginRequiredMixin, CreateView):
    form_class = SubjectTeachersFeedbackReviewForm
    template_name = 'academics/subjectteachers_form.html'

    def form_valid(self, form):
        master = get_object_or_404(SubjectTeachersMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, "Feedback review submitted successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('academics:subjectteachers_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 8. Workflow Transition Views
# -----------------------------------------------------------------------------
class SubjectTeachersWorkflowTransitionCreateView(LoginRequiredMixin, CreateView):
    form_class = SubjectTeachersWorkflowTransitionForm
    template_name = 'academics/subjectteachers_form.html'

    def form_valid(self, form):
        master = get_object_or_404(SubjectTeachersMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        form.instance.actor_username = self.request.user.username
        if form.instance.is_approved and form.instance.to_stage in master.StatusChoices.values:
            master.transition_status(form.instance.to_stage, user_username=self.request.user.username)
        messages.success(self.request, f"Workflow transitioned to {form.instance.to_stage}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('academics:subjectteachers_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 9. Access Rule Views
# -----------------------------------------------------------------------------
class SubjectTeachersAccessRuleCreateView(LoginRequiredMixin, CreateView):
    form_class = SubjectTeachersAccessRuleForm
    template_name = 'academics/subjectteachers_form.html'

    def form_valid(self, form):
        master = get_object_or_404(SubjectTeachersMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        form.instance.granted_by = self.request.user.username
        messages.success(self.request, f"Access rule granted for {form.instance.role_allowed}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('academics:subjectteachers_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 10. Configuration Parameter Views
# -----------------------------------------------------------------------------
class SubjectTeachersConfigurationParameterCreateView(LoginRequiredMixin, CreateView):
    form_class = SubjectTeachersConfigurationParameterForm
    template_name = 'academics/subjectteachers_form.html'

    def form_valid(self, form):
        master = get_object_or_404(SubjectTeachersMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, f"Parameter {form.instance.param_key} saved.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('academics:subjectteachers_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 11. Document Attachment Views
# -----------------------------------------------------------------------------
class SubjectTeachersDocumentAttachmentCreateView(LoginRequiredMixin, CreateView):
    form_class = SubjectTeachersDocumentAttachmentForm
    template_name = 'academics/subjectteachers_form.html'

    def form_valid(self, form):
        master = get_object_or_404(SubjectTeachersMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        form.instance.uploaded_by = self.request.user.username
        messages.success(self.request, f"Attached document {form.instance.title}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('academics:subjectteachers_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 12. Bulk Actions & Exporters
# -----------------------------------------------------------------------------
class SubjectTeachersBulkStatusUpdateView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        selected_ids = request.POST.get('selected_ids', '').split(',')
        action = request.POST.get('action')
        ids = [int(i) for i in selected_ids if i.isdigit()]
        if ids:
            qs = SubjectTeachersMaster.objects.filter(pk__in=ids)
            if action == 'ACTIVATE':
                qs.update(status='ACTIVE', updated_by_user=request.user.username)
            elif action == 'SUSPEND':
                qs.update(status='SUSPENDED', updated_by_user=request.user.username)
            elif action == 'ARCHIVE':
                qs.update(status='ARCHIVED', updated_by_user=request.user.username)
            messages.success(request, f"Bulk action '{action}' applied to {len(ids)} records.")
        return redirect('academics:subjectteachers_list')

class SubjectTeachersExportCSVView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="subjectteachers_export_{timezone.now().strftime("%Y%m%d_%H%M%S")}.csv"'
        writer = csv.writer(response)
        writer.writerow(['Code', 'Name', 'Category', 'Tier', 'Priority', 'Status', 'Capacity', 'Occupancy', 'Budget ($)', 'Incurred ($)', 'Start Date', 'End Date'])
        records = SubjectTeachersMaster.objects.all() if 'SubjectTeachersMaster' in globals() else []
        for r in records:
            writer.writerow([r.code, r.name, r.category, r.tier, r.priority, r.status, r.capacity, r.current_occupancy, r.budget_allocated, r.cost_incurred, r.effective_start_date, r.effective_end_date])
        return response

class SubjectTeachersExportJSONView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        qs = SubjectTeachersMaster.objects.all() if 'SubjectTeachersMaster' in globals() else []
        data = [r.to_dict() for r in qs]
        return JsonResponse({'status': 'success', 'data': data}, safe=False)

class SubjectTeachersAPIListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        qs = SubjectTeachersMaster.objects.all() if 'SubjectTeachersMaster' in globals() else []
        q = request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(Q(name__icontains=q) | Q(code__icontains=q))
        data = [r.to_dict() for r in qs[:50]]
        return JsonResponse({'status': 'success', 'count': len(data), 'results': data})

class SubjectTeachersAPIMetricsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        master = get_object_or_404(SubjectTeachersMaster, pk=self.kwargs.get('pk'))
        return JsonResponse({
            'code': master.code,
            'name': master.name,
            'utilization_rate': master.utilization_rate,
            'remaining_headroom': master.remaining_headroom,
            'budget_allocated': float(master.budget_allocated),
            'cost_incurred': float(master.cost_incurred),
            'budget_variance': float(master.net_budget_variance),
            'status': master.status,
        })

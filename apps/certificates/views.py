"""
Views for EduFlow Certificates Generation & QR Verification (Certificates).
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
        CertificatesMaster, CertificatesItem, CertificatesAllocation,
        CertificatesMetricRecord, CertificatesPolicyRule, CertificatesSchedulePeriod,
        CertificatesFeedbackReview, CertificatesWorkflowTransition, CertificatesAccessRule,
        CertificatesConfigurationParameter, CertificatesDocumentAttachment, CertificatesAuditTrail
    )
    from .forms import (
        CertificatesMasterForm, CertificatesItemForm, CertificatesAllocationForm,
        CertificatesMetricRecordForm, CertificatesPolicyRuleForm, CertificatesSchedulePeriodForm,
        CertificatesFeedbackReviewForm, CertificatesWorkflowTransitionForm, CertificatesAccessRuleForm,
        CertificatesConfigurationParameterForm, CertificatesDocumentAttachmentForm, CertificatesFilterForm,
        CertificatesBulkActionForm
    )
except ImportError:
    try:
        from .models import (
            CertificatesMaster, CertificatesItem, CertificatesAllocation,
            CertificatesMetricRecord, CertificatesPolicyRule, CertificatesSchedulePeriod,
            CertificatesFeedbackReview, CertificatesWorkflowTransition, CertificatesAccessRule,
            CertificatesConfigurationParameter, CertificatesDocumentAttachment, CertificatesAuditTrail
        )
        from .forms import (
            CertificatesMasterForm, CertificatesItemForm, CertificatesAllocationForm,
            CertificatesMetricRecordForm, CertificatesPolicyRuleForm, CertificatesSchedulePeriodForm,
            CertificatesFeedbackReviewForm, CertificatesWorkflowTransitionForm, CertificatesAccessRuleForm,
            CertificatesConfigurationParameterForm, CertificatesDocumentAttachmentForm, CertificatesFilterForm,
            CertificatesBulkActionForm
        )
    except ImportError:
        pass

# -----------------------------------------------------------------------------
# 1. Master Entity Views
# -----------------------------------------------------------------------------
class CertificatesListView(LoginRequiredMixin, ListView):
    template_name = 'certificates/certificates_list.html'
    context_object_name = 'records'
    paginate_by = 25

    def get_queryset(self):
        qs = CertificatesMaster.objects.all() if 'CertificatesMaster' in globals() else []
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
        ctx['filter_form'] = CertificatesFilterForm(self.request.GET) if 'CertificatesFilterForm' in globals() else None
        ctx['bulk_form'] = CertificatesBulkActionForm() if 'CertificatesBulkActionForm' in globals() else None
        ctx['total_count'] = CertificatesMaster.objects.count() if 'CertificatesMaster' in globals() else 0
        ctx['active_count'] = CertificatesMaster.objects.filter(status='ACTIVE').count() if 'CertificatesMaster' in globals() else 0
        ctx['pending_count'] = CertificatesMaster.objects.filter(status='PENDING_REVIEW').count() if 'CertificatesMaster' in globals() else 0
        ctx['page_title'] = "Certificates Generation & QR Verification Directory"
        ctx['domain_name'] = "Certificates"
        return ctx

class CertificatesDetailView(LoginRequiredMixin, DetailView):
    template_name = 'certificates/certificates_detail.html'
    context_object_name = 'record'

    def get_object(self):
        return get_object_or_404(CertificatesMaster, pk=self.kwargs.get('pk'))

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

class CertificatesCreateView(LoginRequiredMixin, CreateView):
    template_name = 'certificates/certificates_form.html'
    form_class = CertificatesMasterForm
    success_url = reverse_lazy('certificates:certificates_list')

    def form_valid(self, form):
        form.instance.created_by_user = self.request.user.username
        form.instance.updated_by_user = self.request.user.username
        messages.success(self.request, f"Certificates record '{form.instance.name}' created successfully.")
        return super().form_valid(form)

class CertificatesUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'certificates/certificates_form.html'
    form_class = CertificatesMasterForm
    success_url = reverse_lazy('certificates:certificates_list')

    def get_object(self):
        return get_object_or_404(CertificatesMaster, pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        form.instance.updated_by_user = self.request.user.username
        messages.success(self.request, f"Certificates record updated successfully.")
        return super().form_valid(form)

class CertificatesDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'certificates/certificates_confirm_delete.html'
    success_url = reverse_lazy('certificates:certificates_list')

    def get_object(self):
        return get_object_or_404(CertificatesMaster, pk=self.kwargs.get('pk'))

# -----------------------------------------------------------------------------
# 2. Line Item Views
# -----------------------------------------------------------------------------
class CertificatesItemCreateView(LoginRequiredMixin, CreateView):
    form_class = CertificatesItemForm
    template_name = 'certificates/certificates_form.html'

    def form_valid(self, form):
        master = get_object_or_404(CertificatesMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, f"Added item '{form.instance.title}' to {master.name}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('certificates:certificates_detail', kwargs={'pk': self.kwargs.get('master_pk')})

class CertificatesItemUpdateView(LoginRequiredMixin, UpdateView):
    form_class = CertificatesItemForm
    template_name = 'certificates/certificates_form.html'

    def get_object(self):
        return get_object_or_404(CertificatesItem, pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse('certificates:certificates_detail', kwargs={'pk': self.object.master_id})

class CertificatesItemDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'certificates/certificates_confirm_delete.html'

    def get_object(self):
        return get_object_or_404(CertificatesItem, pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse('certificates:certificates_detail', kwargs={'pk': self.object.master_id})

# -----------------------------------------------------------------------------
# 3. Allocation Views
# -----------------------------------------------------------------------------
class CertificatesAllocationCreateView(LoginRequiredMixin, CreateView):
    form_class = CertificatesAllocationForm
    template_name = 'certificates/certificates_form.html'

    def form_valid(self, form):
        master = get_object_or_404(CertificatesMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, f"Allocated resource to {form.instance.assignee_name}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('certificates:certificates_detail', kwargs={'pk': self.kwargs.get('master_pk')})

class CertificatesAllocationReleaseView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        alloc = get_object_or_404(CertificatesAllocation, pk=self.kwargs.get('pk'))
        alloc.is_active = False
        alloc.end_time = timezone.now()
        alloc.save()
        messages.info(request, f"Allocation for {alloc.assignee_name} released.")
        return redirect('certificates:certificates_detail', pk=alloc.master_id)

# -----------------------------------------------------------------------------
# 4. Metric Record Views
# -----------------------------------------------------------------------------
class CertificatesMetricCreateView(LoginRequiredMixin, CreateView):
    form_class = CertificatesMetricRecordForm
    template_name = 'certificates/certificates_form.html'

    def form_valid(self, form):
        master = get_object_or_404(CertificatesMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, f"Recorded metric {form.instance.metric_name}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('certificates:certificates_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 5. Policy Rule Views
# -----------------------------------------------------------------------------
class CertificatesPolicyRuleCreateView(LoginRequiredMixin, CreateView):
    form_class = CertificatesPolicyRuleForm
    template_name = 'certificates/certificates_form.html'

    def form_valid(self, form):
        master = get_object_or_404(CertificatesMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, f"Configured policy rule {form.instance.rule_name}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('certificates:certificates_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 6. Schedule Period Views
# -----------------------------------------------------------------------------
class CertificatesSchedulePeriodCreateView(LoginRequiredMixin, CreateView):
    form_class = CertificatesSchedulePeriodForm
    template_name = 'certificates/certificates_form.html'

    def form_valid(self, form):
        master = get_object_or_404(CertificatesMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, f"Added schedule period {form.instance.period_title}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('certificates:certificates_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 7. Feedback Review Views
# -----------------------------------------------------------------------------
class CertificatesFeedbackReviewCreateView(LoginRequiredMixin, CreateView):
    form_class = CertificatesFeedbackReviewForm
    template_name = 'certificates/certificates_form.html'

    def form_valid(self, form):
        master = get_object_or_404(CertificatesMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, "Feedback review submitted successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('certificates:certificates_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 8. Workflow Transition Views
# -----------------------------------------------------------------------------
class CertificatesWorkflowTransitionCreateView(LoginRequiredMixin, CreateView):
    form_class = CertificatesWorkflowTransitionForm
    template_name = 'certificates/certificates_form.html'

    def form_valid(self, form):
        master = get_object_or_404(CertificatesMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        form.instance.actor_username = self.request.user.username
        if form.instance.is_approved and form.instance.to_stage in master.StatusChoices.values:
            master.transition_status(form.instance.to_stage, user_username=self.request.user.username)
        messages.success(self.request, f"Workflow transitioned to {form.instance.to_stage}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('certificates:certificates_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 9. Access Rule Views
# -----------------------------------------------------------------------------
class CertificatesAccessRuleCreateView(LoginRequiredMixin, CreateView):
    form_class = CertificatesAccessRuleForm
    template_name = 'certificates/certificates_form.html'

    def form_valid(self, form):
        master = get_object_or_404(CertificatesMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        form.instance.granted_by = self.request.user.username
        messages.success(self.request, f"Access rule granted for {form.instance.role_allowed}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('certificates:certificates_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 10. Configuration Parameter Views
# -----------------------------------------------------------------------------
class CertificatesConfigurationParameterCreateView(LoginRequiredMixin, CreateView):
    form_class = CertificatesConfigurationParameterForm
    template_name = 'certificates/certificates_form.html'

    def form_valid(self, form):
        master = get_object_or_404(CertificatesMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, f"Parameter {form.instance.param_key} saved.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('certificates:certificates_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 11. Document Attachment Views
# -----------------------------------------------------------------------------
class CertificatesDocumentAttachmentCreateView(LoginRequiredMixin, CreateView):
    form_class = CertificatesDocumentAttachmentForm
    template_name = 'certificates/certificates_form.html'

    def form_valid(self, form):
        master = get_object_or_404(CertificatesMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        form.instance.uploaded_by = self.request.user.username
        messages.success(self.request, f"Attached document {form.instance.title}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('certificates:certificates_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 12. Bulk Actions & Exporters
# -----------------------------------------------------------------------------
class CertificatesBulkStatusUpdateView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        selected_ids = request.POST.get('selected_ids', '').split(',')
        action = request.POST.get('action')
        ids = [int(i) for i in selected_ids if i.isdigit()]
        if ids:
            qs = CertificatesMaster.objects.filter(pk__in=ids)
            if action == 'ACTIVATE':
                qs.update(status='ACTIVE', updated_by_user=request.user.username)
            elif action == 'SUSPEND':
                qs.update(status='SUSPENDED', updated_by_user=request.user.username)
            elif action == 'ARCHIVE':
                qs.update(status='ARCHIVED', updated_by_user=request.user.username)
            messages.success(request, f"Bulk action '{action}' applied to {len(ids)} records.")
        return redirect('certificates:certificates_list')

class CertificatesExportCSVView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="certificates_export_{timezone.now().strftime("%Y%m%d_%H%M%S")}.csv"'
        writer = csv.writer(response)
        writer.writerow(['Code', 'Name', 'Category', 'Tier', 'Priority', 'Status', 'Capacity', 'Occupancy', 'Budget ($)', 'Incurred ($)', 'Start Date', 'End Date'])
        records = CertificatesMaster.objects.all() if 'CertificatesMaster' in globals() else []
        for r in records:
            writer.writerow([r.code, r.name, r.category, r.tier, r.priority, r.status, r.capacity, r.current_occupancy, r.budget_allocated, r.cost_incurred, r.effective_start_date, r.effective_end_date])
        return response

class CertificatesExportJSONView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        qs = CertificatesMaster.objects.all() if 'CertificatesMaster' in globals() else []
        data = [r.to_dict() for r in qs]
        return JsonResponse({'status': 'success', 'data': data}, safe=False)

class CertificatesAPIListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        qs = CertificatesMaster.objects.all() if 'CertificatesMaster' in globals() else []
        q = request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(Q(name__icontains=q) | Q(code__icontains=q))
        data = [r.to_dict() for r in qs[:50]]
        return JsonResponse({'status': 'success', 'count': len(data), 'results': data})

class CertificatesAPIMetricsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        master = get_object_or_404(CertificatesMaster, pk=self.kwargs.get('pk'))
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

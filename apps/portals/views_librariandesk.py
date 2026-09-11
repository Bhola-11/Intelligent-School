"""
Views for EduFlow Librarian Operations Center (LibrarianDesk).
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
        LibrarianDeskMaster, LibrarianDeskItem, LibrarianDeskAllocation,
        LibrarianDeskMetricRecord, LibrarianDeskPolicyRule, LibrarianDeskSchedulePeriod,
        LibrarianDeskFeedbackReview, LibrarianDeskWorkflowTransition, LibrarianDeskAccessRule,
        LibrarianDeskConfigurationParameter, LibrarianDeskDocumentAttachment, LibrarianDeskAuditTrail
    )
    from .forms import (
        LibrarianDeskMasterForm, LibrarianDeskItemForm, LibrarianDeskAllocationForm,
        LibrarianDeskMetricRecordForm, LibrarianDeskPolicyRuleForm, LibrarianDeskSchedulePeriodForm,
        LibrarianDeskFeedbackReviewForm, LibrarianDeskWorkflowTransitionForm, LibrarianDeskAccessRuleForm,
        LibrarianDeskConfigurationParameterForm, LibrarianDeskDocumentAttachmentForm, LibrarianDeskFilterForm,
        LibrarianDeskBulkActionForm
    )
except ImportError:
    try:
        from .models_librariandesk import (
            LibrarianDeskMaster, LibrarianDeskItem, LibrarianDeskAllocation,
            LibrarianDeskMetricRecord, LibrarianDeskPolicyRule, LibrarianDeskSchedulePeriod,
            LibrarianDeskFeedbackReview, LibrarianDeskWorkflowTransition, LibrarianDeskAccessRule,
            LibrarianDeskConfigurationParameter, LibrarianDeskDocumentAttachment, LibrarianDeskAuditTrail
        )
        from .forms_librariandesk import (
            LibrarianDeskMasterForm, LibrarianDeskItemForm, LibrarianDeskAllocationForm,
            LibrarianDeskMetricRecordForm, LibrarianDeskPolicyRuleForm, LibrarianDeskSchedulePeriodForm,
            LibrarianDeskFeedbackReviewForm, LibrarianDeskWorkflowTransitionForm, LibrarianDeskAccessRuleForm,
            LibrarianDeskConfigurationParameterForm, LibrarianDeskDocumentAttachmentForm, LibrarianDeskFilterForm,
            LibrarianDeskBulkActionForm
        )
    except ImportError:
        pass

# -----------------------------------------------------------------------------
# 1. Master Entity Views
# -----------------------------------------------------------------------------
class LibrarianDeskListView(LoginRequiredMixin, ListView):
    template_name = 'portals/librariandesk_list.html'
    context_object_name = 'records'
    paginate_by = 25

    def get_queryset(self):
        qs = LibrarianDeskMaster.objects.all() if 'LibrarianDeskMaster' in globals() else []
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
        ctx['filter_form'] = LibrarianDeskFilterForm(self.request.GET) if 'LibrarianDeskFilterForm' in globals() else None
        ctx['bulk_form'] = LibrarianDeskBulkActionForm() if 'LibrarianDeskBulkActionForm' in globals() else None
        ctx['total_count'] = LibrarianDeskMaster.objects.count() if 'LibrarianDeskMaster' in globals() else 0
        ctx['active_count'] = LibrarianDeskMaster.objects.filter(status='ACTIVE').count() if 'LibrarianDeskMaster' in globals() else 0
        ctx['pending_count'] = LibrarianDeskMaster.objects.filter(status='PENDING_REVIEW').count() if 'LibrarianDeskMaster' in globals() else 0
        ctx['page_title'] = "Librarian Operations Center Directory"
        ctx['domain_name'] = "LibrarianDesk"
        return ctx

class LibrarianDeskDetailView(LoginRequiredMixin, DetailView):
    template_name = 'portals/librariandesk_detail.html'
    context_object_name = 'record'

    def get_object(self):
        return get_object_or_404(LibrarianDeskMaster, pk=self.kwargs.get('pk'))

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

class LibrarianDeskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'portals/librariandesk_form.html'
    form_class = LibrarianDeskMasterForm
    success_url = reverse_lazy('portals:librariandesk_list')

    def form_valid(self, form):
        form.instance.created_by_user = self.request.user.username
        form.instance.updated_by_user = self.request.user.username
        messages.success(self.request, f"LibrarianDesk record '{form.instance.name}' created successfully.")
        return super().form_valid(form)

class LibrarianDeskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'portals/librariandesk_form.html'
    form_class = LibrarianDeskMasterForm
    success_url = reverse_lazy('portals:librariandesk_list')

    def get_object(self):
        return get_object_or_404(LibrarianDeskMaster, pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        form.instance.updated_by_user = self.request.user.username
        messages.success(self.request, f"LibrarianDesk record updated successfully.")
        return super().form_valid(form)

class LibrarianDeskDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'portals/librariandesk_confirm_delete.html'
    success_url = reverse_lazy('portals:librariandesk_list')

    def get_object(self):
        return get_object_or_404(LibrarianDeskMaster, pk=self.kwargs.get('pk'))

# -----------------------------------------------------------------------------
# 2. Line Item Views
# -----------------------------------------------------------------------------
class LibrarianDeskItemCreateView(LoginRequiredMixin, CreateView):
    form_class = LibrarianDeskItemForm
    template_name = 'portals/librariandesk_form.html'

    def form_valid(self, form):
        master = get_object_or_404(LibrarianDeskMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, f"Added item '{form.instance.title}' to {master.name}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('portals:librariandesk_detail', kwargs={'pk': self.kwargs.get('master_pk')})

class LibrarianDeskItemUpdateView(LoginRequiredMixin, UpdateView):
    form_class = LibrarianDeskItemForm
    template_name = 'portals/librariandesk_form.html'

    def get_object(self):
        return get_object_or_404(LibrarianDeskItem, pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse('portals:librariandesk_detail', kwargs={'pk': self.object.master_id})

class LibrarianDeskItemDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'portals/librariandesk_confirm_delete.html'

    def get_object(self):
        return get_object_or_404(LibrarianDeskItem, pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse('portals:librariandesk_detail', kwargs={'pk': self.object.master_id})

# -----------------------------------------------------------------------------
# 3. Allocation Views
# -----------------------------------------------------------------------------
class LibrarianDeskAllocationCreateView(LoginRequiredMixin, CreateView):
    form_class = LibrarianDeskAllocationForm
    template_name = 'portals/librariandesk_form.html'

    def form_valid(self, form):
        master = get_object_or_404(LibrarianDeskMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, f"Allocated resource to {form.instance.assignee_name}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('portals:librariandesk_detail', kwargs={'pk': self.kwargs.get('master_pk')})

class LibrarianDeskAllocationReleaseView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        alloc = get_object_or_404(LibrarianDeskAllocation, pk=self.kwargs.get('pk'))
        alloc.is_active = False
        alloc.end_time = timezone.now()
        alloc.save()
        messages.info(request, f"Allocation for {alloc.assignee_name} released.")
        return redirect('portals:librariandesk_detail', pk=alloc.master_id)

# -----------------------------------------------------------------------------
# 4. Metric Record Views
# -----------------------------------------------------------------------------
class LibrarianDeskMetricCreateView(LoginRequiredMixin, CreateView):
    form_class = LibrarianDeskMetricRecordForm
    template_name = 'portals/librariandesk_form.html'

    def form_valid(self, form):
        master = get_object_or_404(LibrarianDeskMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, f"Recorded metric {form.instance.metric_name}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('portals:librariandesk_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 5. Policy Rule Views
# -----------------------------------------------------------------------------
class LibrarianDeskPolicyRuleCreateView(LoginRequiredMixin, CreateView):
    form_class = LibrarianDeskPolicyRuleForm
    template_name = 'portals/librariandesk_form.html'

    def form_valid(self, form):
        master = get_object_or_404(LibrarianDeskMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, f"Configured policy rule {form.instance.rule_name}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('portals:librariandesk_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 6. Schedule Period Views
# -----------------------------------------------------------------------------
class LibrarianDeskSchedulePeriodCreateView(LoginRequiredMixin, CreateView):
    form_class = LibrarianDeskSchedulePeriodForm
    template_name = 'portals/librariandesk_form.html'

    def form_valid(self, form):
        master = get_object_or_404(LibrarianDeskMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, f"Added schedule period {form.instance.period_title}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('portals:librariandesk_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 7. Feedback Review Views
# -----------------------------------------------------------------------------
class LibrarianDeskFeedbackReviewCreateView(LoginRequiredMixin, CreateView):
    form_class = LibrarianDeskFeedbackReviewForm
    template_name = 'portals/librariandesk_form.html'

    def form_valid(self, form):
        master = get_object_or_404(LibrarianDeskMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, "Feedback review submitted successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('portals:librariandesk_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 8. Workflow Transition Views
# -----------------------------------------------------------------------------
class LibrarianDeskWorkflowTransitionCreateView(LoginRequiredMixin, CreateView):
    form_class = LibrarianDeskWorkflowTransitionForm
    template_name = 'portals/librariandesk_form.html'

    def form_valid(self, form):
        master = get_object_or_404(LibrarianDeskMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        form.instance.actor_username = self.request.user.username
        if form.instance.is_approved and form.instance.to_stage in master.StatusChoices.values:
            master.transition_status(form.instance.to_stage, user_username=self.request.user.username)
        messages.success(self.request, f"Workflow transitioned to {form.instance.to_stage}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('portals:librariandesk_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 9. Access Rule Views
# -----------------------------------------------------------------------------
class LibrarianDeskAccessRuleCreateView(LoginRequiredMixin, CreateView):
    form_class = LibrarianDeskAccessRuleForm
    template_name = 'portals/librariandesk_form.html'

    def form_valid(self, form):
        master = get_object_or_404(LibrarianDeskMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        form.instance.granted_by = self.request.user.username
        messages.success(self.request, f"Access rule granted for {form.instance.role_allowed}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('portals:librariandesk_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 10. Configuration Parameter Views
# -----------------------------------------------------------------------------
class LibrarianDeskConfigurationParameterCreateView(LoginRequiredMixin, CreateView):
    form_class = LibrarianDeskConfigurationParameterForm
    template_name = 'portals/librariandesk_form.html'

    def form_valid(self, form):
        master = get_object_or_404(LibrarianDeskMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        messages.success(self.request, f"Parameter {form.instance.param_key} saved.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('portals:librariandesk_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 11. Document Attachment Views
# -----------------------------------------------------------------------------
class LibrarianDeskDocumentAttachmentCreateView(LoginRequiredMixin, CreateView):
    form_class = LibrarianDeskDocumentAttachmentForm
    template_name = 'portals/librariandesk_form.html'

    def form_valid(self, form):
        master = get_object_or_404(LibrarianDeskMaster, pk=self.kwargs.get('master_pk'))
        form.instance.master = master
        form.instance.uploaded_by = self.request.user.username
        messages.success(self.request, f"Attached document {form.instance.title}.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('portals:librariandesk_detail', kwargs={'pk': self.kwargs.get('master_pk')})

# -----------------------------------------------------------------------------
# 12. Bulk Actions & Exporters
# -----------------------------------------------------------------------------
class LibrarianDeskBulkStatusUpdateView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        selected_ids = request.POST.get('selected_ids', '').split(',')
        action = request.POST.get('action')
        ids = [int(i) for i in selected_ids if i.isdigit()]
        if ids:
            qs = LibrarianDeskMaster.objects.filter(pk__in=ids)
            if action == 'ACTIVATE':
                qs.update(status='ACTIVE', updated_by_user=request.user.username)
            elif action == 'SUSPEND':
                qs.update(status='SUSPENDED', updated_by_user=request.user.username)
            elif action == 'ARCHIVE':
                qs.update(status='ARCHIVED', updated_by_user=request.user.username)
            messages.success(request, f"Bulk action '{action}' applied to {len(ids)} records.")
        return redirect('portals:librariandesk_list')

class LibrarianDeskExportCSVView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="librariandesk_export_{timezone.now().strftime("%Y%m%d_%H%M%S")}.csv"'
        writer = csv.writer(response)
        writer.writerow(['Code', 'Name', 'Category', 'Tier', 'Priority', 'Status', 'Capacity', 'Occupancy', 'Budget ($)', 'Incurred ($)', 'Start Date', 'End Date'])
        records = LibrarianDeskMaster.objects.all() if 'LibrarianDeskMaster' in globals() else []
        for r in records:
            writer.writerow([r.code, r.name, r.category, r.tier, r.priority, r.status, r.capacity, r.current_occupancy, r.budget_allocated, r.cost_incurred, r.effective_start_date, r.effective_end_date])
        return response

class LibrarianDeskExportJSONView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        qs = LibrarianDeskMaster.objects.all() if 'LibrarianDeskMaster' in globals() else []
        data = [r.to_dict() for r in qs]
        return JsonResponse({'status': 'success', 'data': data}, safe=False)

class LibrarianDeskAPIListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        qs = LibrarianDeskMaster.objects.all() if 'LibrarianDeskMaster' in globals() else []
        q = request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(Q(name__icontains=q) | Q(code__icontains=q))
        data = [r.to_dict() for r in qs[:50]]
        return JsonResponse({'status': 'success', 'count': len(data), 'results': data})

class LibrarianDeskAPIMetricsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        master = get_object_or_404(LibrarianDeskMaster, pk=self.kwargs.get('pk'))
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

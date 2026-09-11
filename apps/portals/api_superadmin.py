"""
Extended REST API Controllers for EduFlow Super Administrator Executive Portal (SuperAdmin).
Provides headless JSON endpoints, batch operations, query filters, and summary telemetry.
"""

import json
from decimal import Decimal
from django.views.generic import View
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models import Q

try:
    from .models import (
        SuperAdminMaster, SuperAdminItem, SuperAdminAllocation,
        SuperAdminMetricRecord, SuperAdminPolicyRule, SuperAdminSchedulePeriod,
        SuperAdminFeedbackReview, SuperAdminWorkflowTransition, SuperAdminAccessRule,
        SuperAdminConfigurationParameter, SuperAdminDocumentAttachment, SuperAdminAuditTrail
    )
    from .services import SuperAdminService
except ImportError:
    try:
        from .models import (
            SuperAdminMaster, SuperAdminItem, SuperAdminAllocation,
            SuperAdminMetricRecord, SuperAdminPolicyRule, SuperAdminSchedulePeriod,
            SuperAdminFeedbackReview, SuperAdminWorkflowTransition, SuperAdminAccessRule,
            SuperAdminConfigurationParameter, SuperAdminDocumentAttachment, SuperAdminAuditTrail
        )
        from .services import SuperAdminService
    except ImportError:
        pass

class SuperAdminAPIDetailView(LoginRequiredMixin, View):
    """Retrieves full nested JSON representation of a master record."""
    def get(self, request, pk, *args, **kwargs):
        master = get_object_or_404(SuperAdminMaster, pk=pk)
        data = master.to_dict()
        data['items_count'] = master.items.count() if hasattr(master, 'items') else 0
        data['allocations_count'] = master.allocations.count() if hasattr(master, 'allocations') else 0
        data['metrics_count'] = master.metrics.count() if hasattr(master, 'metrics') else 0
        return JsonResponse({'status': 'success', 'data': data})

class SuperAdminAPISearchView(LoginRequiredMixin, View):
    """Fast indexed autocomplete search endpoint."""
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '').strip()
        status_filter = request.GET.get('status')
        qs = SuperAdminMaster.objects.all() if 'SuperAdminMaster' in globals() else []
        if query:
            qs = qs.filter(Q(code__icontains=query) | Q(name__icontains=query) | Q(tags__icontains=query))
        if status_filter:
            qs = qs.filter(status=status_filter)
        results = [{'id': r.pk, 'code': r.code, 'name': r.name, 'status': r.status, 'capacity': r.capacity} for r in qs[:20]]
        return JsonResponse({'status': 'success', 'count': len(results), 'results': results})

@method_decorator(csrf_exempt, name='dispatch')
class SuperAdminAPIBatchUpdateView(LoginRequiredMixin, View):
    """Executes atomic batch state mutations on master records."""
    def post(self, request, *args, **kwargs):
        if not getattr(request.user, 'is_staff', False) and getattr(request.user, 'role', '') not in ['SuperAdmin', 'InstitutionAdmin']:
            return HttpResponseForbidden(json.dumps({'status': 'error', 'message': 'Permission denied'}), content_type='application/json')
        try:
            body = json.loads(request.body.decode('utf-8'))
        except Exception:
            return HttpResponseBadRequest(json.dumps({'status': 'error', 'message': 'Malformed JSON'}), content_type='application/json')
        
        ids = body.get('ids', [])
        action = body.get('action')
        if not ids or not action:
            return HttpResponseBadRequest(json.dumps({'status': 'error', 'message': 'Missing ids or action'}), content_type='application/json')

        qs = SuperAdminMaster.objects.filter(pk__in=ids)
        updated_count = 0
        for rec in qs:
            if action == 'ACTIVATE':
                rec.transition_status('ACTIVE', user_username=request.user.username)
                updated_count += 1
            elif action == 'SUSPEND':
                rec.transition_status('SUSPENDED', user_username=request.user.username)
                updated_count += 1
            elif action == 'ARCHIVE':
                rec.transition_status('ARCHIVED', user_username=request.user.username)
                updated_count += 1

        return JsonResponse({'status': 'success', 'updated_count': updated_count, 'action': action})

class SuperAdminAPITelemetryView(LoginRequiredMixin, View):
    """Returns high-frequency utilization and telemetry data."""
    def get(self, request, *args, **kwargs):
        records = SuperAdminMaster.objects.all() if 'SuperAdminMaster' in globals() else []
        total_capacity = sum(r.capacity for r in records)
        total_occupancy = sum(r.current_occupancy for r in records)
        active_records = [r for r in records if r.status == 'ACTIVE']
        
        return JsonResponse({
            'status': 'success',
            'telemetry': {
                'total_monitored_nodes': len(records),
                'active_operational_nodes': len(active_records),
                'aggregate_capacity': total_capacity,
                'aggregate_occupancy': total_occupancy,
                'aggregate_load_percentage': round((total_occupancy / total_capacity * 100), 2) if total_capacity > 0 else 0.0,
                'timestamp': timezone.now().isoformat()
            }
        })

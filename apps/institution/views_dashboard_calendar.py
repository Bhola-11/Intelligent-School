"""
Operational Dashboard and Realtime KPI Analytics for EduFlow Academic Calendar, Terms & Semesters (Calendar).
Includes executive metric cards, status breakdown distribution, and recent audit logs.
"""

from decimal import Decimal
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Sum, Avg, Q
from django.utils import timezone

try:
    from .models import (
        CalendarMaster, CalendarItem, CalendarAllocation,
        CalendarMetricRecord, CalendarPolicyRule, CalendarSchedulePeriod,
        CalendarFeedbackReview, CalendarWorkflowTransition, CalendarAccessRule,
        CalendarConfigurationParameter, CalendarDocumentAttachment, CalendarAuditTrail
    )
except ImportError:
    try:
        from .models_calendar import (
            CalendarMaster, CalendarItem, CalendarAllocation,
            CalendarMetricRecord, CalendarPolicyRule, CalendarSchedulePeriod,
            CalendarFeedbackReview, CalendarWorkflowTransition, CalendarAccessRule,
            CalendarConfigurationParameter, CalendarDocumentAttachment, CalendarAuditTrail
        )
    except ImportError:
        pass

class CalendarDashboardView(LoginRequiredMixin, TemplateView):
    """Executive operations dashboard for Calendar."""
    template_name = 'institution/calendar_dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        records = CalendarMaster.objects.all() if 'CalendarMaster' in globals() else []

        total_count = len(records)
        active_count = len([r for r in records if r.status == 'ACTIVE'])
        pending_count = len([r for r in records if r.status in ['DRAFT', 'PENDING_REVIEW']])
        archived_count = len([r for r in records if r.status == 'ARCHIVED'])

        total_capacity = sum(r.capacity for r in records)
        total_occupancy = sum(r.current_occupancy for r in records)
        overall_util = round((total_occupancy / total_capacity * 100), 2) if total_capacity > 0 else 0.0

        total_budget = sum(r.budget_allocated for r in records)
        total_spent = sum(r.cost_incurred for r in records)
        variance = total_budget - total_spent

        # Recent activities
        audit_trail = CalendarAuditTrail.objects.all().order_by('-timestamp')[:10] if 'CalendarAuditTrail' in globals() else []
        recent_records = records[:8] if records else []

        ctx.update({
            "page_title": "Academic Calendar, Terms & Semesters Operations Dashboard",
            'domain_name': 'Calendar',
            'app_title': 'Institution',
            'total_count': total_count,
            'active_count': active_count,
            'pending_count': pending_count,
            'archived_count': archived_count,
            'total_capacity': total_capacity,
            'total_occupancy': total_occupancy,
            'overall_util': overall_util,
            'total_budget': total_budget,
            'total_spent': total_spent,
            'variance': variance,
            'audit_trail': audit_trail,
            'recent_records': recent_records,
            'timestamp': timezone.now(),
        })
        return ctx

class CalendarAnalyticsView(LoginRequiredMixin, TemplateView):
    """Detailed analytics report view with chart telemetry data."""
    template_name = 'institution/calendar_analytics.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        records = CalendarMaster.objects.all() if 'CalendarMaster' in globals() else []

        tier_breakdown = {}
        for r in records:
            tier_breakdown[r.tier] = tier_breakdown.get(r.tier, 0) + 1

        priority_breakdown = {}
        for r in records:
            priority_breakdown[r.priority] = priority_breakdown.get(r.priority, 0) + 1

        ctx.update({
            "page_title": "Academic Calendar, Terms & Semesters Analytical Insights",
            'tier_breakdown': tier_breakdown,
            'priority_breakdown': priority_breakdown,
            'total_records': len(records),
        })
        return ctx

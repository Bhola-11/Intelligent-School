"""URL Routing for EduFlow Leave Policies & Entitlement Setup (LeavePolicies)."""
from django.urls import path
try:
    from . import views_leavepolicies as views
except ImportError:
    from . import views

app_name = 'leaves'

urlpatterns = [
    path('leavepolicies/', getattr(views, 'LeavePoliciesListView').as_view(), name='leavepolicies_list'),
    path('leavepolicies/create/', getattr(views, 'LeavePoliciesCreateView').as_view(), name='leavepolicies_create'),
    path('leavepolicies/<int:pk>/', getattr(views, 'LeavePoliciesDetailView').as_view(), name='leavepolicies_detail'),
    path('leavepolicies/<int:pk>/edit/', getattr(views, 'LeavePoliciesUpdateView').as_view(), name='leavepolicies_edit'),
    path('leavepolicies/<int:pk>/delete/', getattr(views, 'LeavePoliciesDeleteView').as_view(), name='leavepolicies_delete'),
    path('leavepolicies/<int:master_pk>/add-item/', getattr(views, 'LeavePoliciesItemCreateView').as_view(), name='leavepolicies_add_item'),
    path('leavepolicies/<int:master_pk>/allocate/', getattr(views, 'LeavePoliciesAllocationCreateView').as_view(), name='leavepolicies_allocate'),
    path('leavepolicies/bulk-update/', getattr(views, 'LeavePoliciesBulkStatusUpdateView').as_view(), name='leavepolicies_bulk_update'),
    path('leavepolicies/export/csv/', getattr(views, 'LeavePoliciesExportCSVView').as_view(), name='leavepolicies_export_csv'),
    path('leavepolicies/export/json/', getattr(views, 'LeavePoliciesExportJSONView').as_view(), name='leavepolicies_export_json'),
    path('leavepolicies/api/list/', getattr(views, 'LeavePoliciesAPIListView').as_view(), name='leavepolicies_api_list'),
    path('leavepolicies/<int:pk>/api/metrics/', getattr(views, 'LeavePoliciesAPIMetricsView').as_view(), name='leavepolicies_api_metrics'),
    path('leavepolicies/dashboard/', getattr(views, 'LeavePoliciesDashboardView', getattr(views, 'LeavePoliciesListView')).as_view(), name='leavepolicies_dashboard'),
    path('leavepolicies/analytics/', getattr(views, 'LeavePoliciesAnalyticsView', getattr(views, 'LeavePoliciesListView')).as_view(), name='leavepolicies_analytics'),
]

"""URL Routing for EduFlow Teacher Workload & Teaching Allocations (Workload)."""
from django.urls import path
try:
    from . import views_workload as views
except ImportError:
    from . import views

app_name = 'staff'

urlpatterns = [
    path('workload/', getattr(views, 'WorkloadListView').as_view(), name='workload_list'),
    path('workload/create/', getattr(views, 'WorkloadCreateView').as_view(), name='workload_create'),
    path('workload/<int:pk>/', getattr(views, 'WorkloadDetailView').as_view(), name='workload_detail'),
    path('workload/<int:pk>/edit/', getattr(views, 'WorkloadUpdateView').as_view(), name='workload_edit'),
    path('workload/<int:pk>/delete/', getattr(views, 'WorkloadDeleteView').as_view(), name='workload_delete'),
    path('workload/<int:master_pk>/add-item/', getattr(views, 'WorkloadItemCreateView').as_view(), name='workload_add_item'),
    path('workload/<int:master_pk>/allocate/', getattr(views, 'WorkloadAllocationCreateView').as_view(), name='workload_allocate'),
    path('workload/bulk-update/', getattr(views, 'WorkloadBulkStatusUpdateView').as_view(), name='workload_bulk_update'),
    path('workload/export/csv/', getattr(views, 'WorkloadExportCSVView').as_view(), name='workload_export_csv'),
    path('workload/export/json/', getattr(views, 'WorkloadExportJSONView').as_view(), name='workload_export_json'),
    path('workload/api/list/', getattr(views, 'WorkloadAPIListView').as_view(), name='workload_api_list'),
    path('workload/<int:pk>/api/metrics/', getattr(views, 'WorkloadAPIMetricsView').as_view(), name='workload_api_metrics'),
    path('workload/dashboard/', getattr(views, 'WorkloadDashboardView', getattr(views, 'WorkloadListView')).as_view(), name='workload_dashboard'),
    path('workload/analytics/', getattr(views, 'WorkloadAnalyticsView', getattr(views, 'WorkloadListView')).as_view(), name='workload_analytics'),
]

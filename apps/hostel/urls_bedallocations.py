"""URL Routing for EduFlow Hostel Bed Allocation & Check-In (BedAllocations)."""
from django.urls import path
try:
    from . import views_bedallocations as views
except ImportError:
    from . import views

app_name = 'hostel'

urlpatterns = [
    path('bedallocations/', getattr(views, 'BedAllocationsListView').as_view(), name='bedallocations_list'),
    path('bedallocations/create/', getattr(views, 'BedAllocationsCreateView').as_view(), name='bedallocations_create'),
    path('bedallocations/<int:pk>/', getattr(views, 'BedAllocationsDetailView').as_view(), name='bedallocations_detail'),
    path('bedallocations/<int:pk>/edit/', getattr(views, 'BedAllocationsUpdateView').as_view(), name='bedallocations_edit'),
    path('bedallocations/<int:pk>/delete/', getattr(views, 'BedAllocationsDeleteView').as_view(), name='bedallocations_delete'),
    path('bedallocations/<int:master_pk>/add-item/', getattr(views, 'BedAllocationsItemCreateView').as_view(), name='bedallocations_add_item'),
    path('bedallocations/<int:master_pk>/allocate/', getattr(views, 'BedAllocationsAllocationCreateView').as_view(), name='bedallocations_allocate'),
    path('bedallocations/bulk-update/', getattr(views, 'BedAllocationsBulkStatusUpdateView').as_view(), name='bedallocations_bulk_update'),
    path('bedallocations/export/csv/', getattr(views, 'BedAllocationsExportCSVView').as_view(), name='bedallocations_export_csv'),
    path('bedallocations/export/json/', getattr(views, 'BedAllocationsExportJSONView').as_view(), name='bedallocations_export_json'),
    path('bedallocations/api/list/', getattr(views, 'BedAllocationsAPIListView').as_view(), name='bedallocations_api_list'),
    path('bedallocations/<int:pk>/api/metrics/', getattr(views, 'BedAllocationsAPIMetricsView').as_view(), name='bedallocations_api_metrics'),
    path('bedallocations/dashboard/', getattr(views, 'BedAllocationsDashboardView', getattr(views, 'BedAllocationsListView')).as_view(), name='bedallocations_dashboard'),
    path('bedallocations/analytics/', getattr(views, 'BedAllocationsAnalyticsView', getattr(views, 'BedAllocationsListView')).as_view(), name='bedallocations_analytics'),
]

"""URL Routing for EduFlow Asset Allocations, Stock Movement & Depreciations (AssetAllocations)."""
from django.urls import path
try:
    from . import views_assetallocations as views
except ImportError:
    from . import views

app_name = 'inventory'

urlpatterns = [
    path('assetallocations/', getattr(views, 'AssetAllocationsListView').as_view(), name='assetallocations_list'),
    path('assetallocations/create/', getattr(views, 'AssetAllocationsCreateView').as_view(), name='assetallocations_create'),
    path('assetallocations/<int:pk>/', getattr(views, 'AssetAllocationsDetailView').as_view(), name='assetallocations_detail'),
    path('assetallocations/<int:pk>/edit/', getattr(views, 'AssetAllocationsUpdateView').as_view(), name='assetallocations_edit'),
    path('assetallocations/<int:pk>/delete/', getattr(views, 'AssetAllocationsDeleteView').as_view(), name='assetallocations_delete'),
    path('assetallocations/<int:master_pk>/add-item/', getattr(views, 'AssetAllocationsItemCreateView').as_view(), name='assetallocations_add_item'),
    path('assetallocations/<int:master_pk>/allocate/', getattr(views, 'AssetAllocationsAllocationCreateView').as_view(), name='assetallocations_allocate'),
    path('assetallocations/bulk-update/', getattr(views, 'AssetAllocationsBulkStatusUpdateView').as_view(), name='assetallocations_bulk_update'),
    path('assetallocations/export/csv/', getattr(views, 'AssetAllocationsExportCSVView').as_view(), name='assetallocations_export_csv'),
    path('assetallocations/export/json/', getattr(views, 'AssetAllocationsExportJSONView').as_view(), name='assetallocations_export_json'),
    path('assetallocations/api/list/', getattr(views, 'AssetAllocationsAPIListView').as_view(), name='assetallocations_api_list'),
    path('assetallocations/<int:pk>/api/metrics/', getattr(views, 'AssetAllocationsAPIMetricsView').as_view(), name='assetallocations_api_metrics'),
    path('assetallocations/dashboard/', getattr(views, 'AssetAllocationsDashboardView', getattr(views, 'AssetAllocationsListView')).as_view(), name='assetallocations_dashboard'),
    path('assetallocations/analytics/', getattr(views, 'AssetAllocationsAnalyticsView', getattr(views, 'AssetAllocationsListView')).as_view(), name='assetallocations_analytics'),
]

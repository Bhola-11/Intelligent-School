"""URL Routing for EduFlow Inventory Categories & Asset Registry (AssetRegistry)."""
from django.urls import path
try:
    from . import views_assetregistry as views
except ImportError:
    from . import views

app_name = 'inventory'

urlpatterns = [
    path('assetregistry/', getattr(views, 'AssetRegistryListView').as_view(), name='assetregistry_list'),
    path('assetregistry/create/', getattr(views, 'AssetRegistryCreateView').as_view(), name='assetregistry_create'),
    path('assetregistry/<int:pk>/', getattr(views, 'AssetRegistryDetailView').as_view(), name='assetregistry_detail'),
    path('assetregistry/<int:pk>/edit/', getattr(views, 'AssetRegistryUpdateView').as_view(), name='assetregistry_edit'),
    path('assetregistry/<int:pk>/delete/', getattr(views, 'AssetRegistryDeleteView').as_view(), name='assetregistry_delete'),
    path('assetregistry/<int:master_pk>/add-item/', getattr(views, 'AssetRegistryItemCreateView').as_view(), name='assetregistry_add_item'),
    path('assetregistry/<int:master_pk>/allocate/', getattr(views, 'AssetRegistryAllocationCreateView').as_view(), name='assetregistry_allocate'),
    path('assetregistry/bulk-update/', getattr(views, 'AssetRegistryBulkStatusUpdateView').as_view(), name='assetregistry_bulk_update'),
    path('assetregistry/export/csv/', getattr(views, 'AssetRegistryExportCSVView').as_view(), name='assetregistry_export_csv'),
    path('assetregistry/export/json/', getattr(views, 'AssetRegistryExportJSONView').as_view(), name='assetregistry_export_json'),
    path('assetregistry/api/list/', getattr(views, 'AssetRegistryAPIListView').as_view(), name='assetregistry_api_list'),
    path('assetregistry/<int:pk>/api/metrics/', getattr(views, 'AssetRegistryAPIMetricsView').as_view(), name='assetregistry_api_metrics'),
    path('assetregistry/dashboard/', getattr(views, 'AssetRegistryDashboardView', getattr(views, 'AssetRegistryListView')).as_view(), name='assetregistry_dashboard'),
    path('assetregistry/analytics/', getattr(views, 'AssetRegistryAnalyticsView', getattr(views, 'AssetRegistryListView')).as_view(), name='assetregistry_analytics'),
]

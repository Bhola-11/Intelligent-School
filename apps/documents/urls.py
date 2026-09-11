"""URL Routing for EduFlow Institutional Document Vault & Access Control (DocumentVault)."""
from django.urls import path
try:
    from . import views_documentvault as views
except ImportError:
    from . import views

app_name = 'documents'

urlpatterns = [
    path('documentvault/', getattr(views, 'DocumentVaultListView').as_view(), name='documentvault_list'),
    path('documentvault/create/', getattr(views, 'DocumentVaultCreateView').as_view(), name='documentvault_create'),
    path('documentvault/<int:pk>/', getattr(views, 'DocumentVaultDetailView').as_view(), name='documentvault_detail'),
    path('documentvault/<int:pk>/edit/', getattr(views, 'DocumentVaultUpdateView').as_view(), name='documentvault_edit'),
    path('documentvault/<int:pk>/delete/', getattr(views, 'DocumentVaultDeleteView').as_view(), name='documentvault_delete'),
    path('documentvault/<int:master_pk>/add-item/', getattr(views, 'DocumentVaultItemCreateView').as_view(), name='documentvault_add_item'),
    path('documentvault/<int:master_pk>/allocate/', getattr(views, 'DocumentVaultAllocationCreateView').as_view(), name='documentvault_allocate'),
    path('documentvault/bulk-update/', getattr(views, 'DocumentVaultBulkStatusUpdateView').as_view(), name='documentvault_bulk_update'),
    path('documentvault/export/csv/', getattr(views, 'DocumentVaultExportCSVView').as_view(), name='documentvault_export_csv'),
    path('documentvault/export/json/', getattr(views, 'DocumentVaultExportJSONView').as_view(), name='documentvault_export_json'),
    path('documentvault/api/list/', getattr(views, 'DocumentVaultAPIListView').as_view(), name='documentvault_api_list'),
    path('documentvault/<int:pk>/api/metrics/', getattr(views, 'DocumentVaultAPIMetricsView').as_view(), name='documentvault_api_metrics'),
    path('documentvault/dashboard/', getattr(views, 'DocumentVaultDashboardView', getattr(views, 'DocumentVaultListView')).as_view(), name='documentvault_dashboard'),
    path('documentvault/analytics/', getattr(views, 'DocumentVaultAnalyticsView', getattr(views, 'DocumentVaultListView')).as_view(), name='documentvault_analytics'),
]

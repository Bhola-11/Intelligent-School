"""URL Routing for EduFlow Student Document Vault & Verifications (Documents)."""
from django.urls import path
try:
    from . import views_documents as views
except ImportError:
    from . import views

app_name = 'students'

urlpatterns = [
    path('documents/', getattr(views, 'DocumentsListView').as_view(), name='documents_list'),
    path('documents/create/', getattr(views, 'DocumentsCreateView').as_view(), name='documents_create'),
    path('documents/<int:pk>/', getattr(views, 'DocumentsDetailView').as_view(), name='documents_detail'),
    path('documents/<int:pk>/edit/', getattr(views, 'DocumentsUpdateView').as_view(), name='documents_edit'),
    path('documents/<int:pk>/delete/', getattr(views, 'DocumentsDeleteView').as_view(), name='documents_delete'),
    path('documents/<int:master_pk>/add-item/', getattr(views, 'DocumentsItemCreateView').as_view(), name='documents_add_item'),
    path('documents/<int:master_pk>/allocate/', getattr(views, 'DocumentsAllocationCreateView').as_view(), name='documents_allocate'),
    path('documents/bulk-update/', getattr(views, 'DocumentsBulkStatusUpdateView').as_view(), name='documents_bulk_update'),
    path('documents/export/csv/', getattr(views, 'DocumentsExportCSVView').as_view(), name='documents_export_csv'),
    path('documents/export/json/', getattr(views, 'DocumentsExportJSONView').as_view(), name='documents_export_json'),
    path('documents/api/list/', getattr(views, 'DocumentsAPIListView').as_view(), name='documents_api_list'),
    path('documents/<int:pk>/api/metrics/', getattr(views, 'DocumentsAPIMetricsView').as_view(), name='documents_api_metrics'),
    path('documents/dashboard/', getattr(views, 'DocumentsDashboardView', getattr(views, 'DocumentsListView')).as_view(), name='documents_dashboard'),
    path('documents/analytics/', getattr(views, 'DocumentsAnalyticsView', getattr(views, 'DocumentsListView')).as_view(), name='documents_analytics'),
]

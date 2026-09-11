"""URL Routing for EduFlow Library Book Catalog & ISBN Management (BookCatalog)."""
from django.urls import path
try:
    from . import views_bookcatalog as views
except ImportError:
    from . import views

app_name = 'library'

urlpatterns = [
    path('bookcatalog/', getattr(views, 'BookCatalogListView').as_view(), name='bookcatalog_list'),
    path('bookcatalog/create/', getattr(views, 'BookCatalogCreateView').as_view(), name='bookcatalog_create'),
    path('bookcatalog/<int:pk>/', getattr(views, 'BookCatalogDetailView').as_view(), name='bookcatalog_detail'),
    path('bookcatalog/<int:pk>/edit/', getattr(views, 'BookCatalogUpdateView').as_view(), name='bookcatalog_edit'),
    path('bookcatalog/<int:pk>/delete/', getattr(views, 'BookCatalogDeleteView').as_view(), name='bookcatalog_delete'),
    path('bookcatalog/<int:master_pk>/add-item/', getattr(views, 'BookCatalogItemCreateView').as_view(), name='bookcatalog_add_item'),
    path('bookcatalog/<int:master_pk>/allocate/', getattr(views, 'BookCatalogAllocationCreateView').as_view(), name='bookcatalog_allocate'),
    path('bookcatalog/bulk-update/', getattr(views, 'BookCatalogBulkStatusUpdateView').as_view(), name='bookcatalog_bulk_update'),
    path('bookcatalog/export/csv/', getattr(views, 'BookCatalogExportCSVView').as_view(), name='bookcatalog_export_csv'),
    path('bookcatalog/export/json/', getattr(views, 'BookCatalogExportJSONView').as_view(), name='bookcatalog_export_json'),
    path('bookcatalog/api/list/', getattr(views, 'BookCatalogAPIListView').as_view(), name='bookcatalog_api_list'),
    path('bookcatalog/<int:pk>/api/metrics/', getattr(views, 'BookCatalogAPIMetricsView').as_view(), name='bookcatalog_api_metrics'),
    path('bookcatalog/dashboard/', getattr(views, 'BookCatalogDashboardView', getattr(views, 'BookCatalogListView')).as_view(), name='bookcatalog_dashboard'),
    path('bookcatalog/analytics/', getattr(views, 'BookCatalogAnalyticsView', getattr(views, 'BookCatalogListView')).as_view(), name='bookcatalog_analytics'),
]

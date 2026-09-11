"""URL Routing for EduFlow Book Copies, Barcodes & Shelf Tracking (BookCopies)."""
from django.urls import path
try:
    from . import views_bookcopies as views
except ImportError:
    from . import views

app_name = 'library'

urlpatterns = [
    path('bookcopies/', getattr(views, 'BookCopiesListView').as_view(), name='bookcopies_list'),
    path('bookcopies/create/', getattr(views, 'BookCopiesCreateView').as_view(), name='bookcopies_create'),
    path('bookcopies/<int:pk>/', getattr(views, 'BookCopiesDetailView').as_view(), name='bookcopies_detail'),
    path('bookcopies/<int:pk>/edit/', getattr(views, 'BookCopiesUpdateView').as_view(), name='bookcopies_edit'),
    path('bookcopies/<int:pk>/delete/', getattr(views, 'BookCopiesDeleteView').as_view(), name='bookcopies_delete'),
    path('bookcopies/<int:master_pk>/add-item/', getattr(views, 'BookCopiesItemCreateView').as_view(), name='bookcopies_add_item'),
    path('bookcopies/<int:master_pk>/allocate/', getattr(views, 'BookCopiesAllocationCreateView').as_view(), name='bookcopies_allocate'),
    path('bookcopies/bulk-update/', getattr(views, 'BookCopiesBulkStatusUpdateView').as_view(), name='bookcopies_bulk_update'),
    path('bookcopies/export/csv/', getattr(views, 'BookCopiesExportCSVView').as_view(), name='bookcopies_export_csv'),
    path('bookcopies/export/json/', getattr(views, 'BookCopiesExportJSONView').as_view(), name='bookcopies_export_json'),
    path('bookcopies/api/list/', getattr(views, 'BookCopiesAPIListView').as_view(), name='bookcopies_api_list'),
    path('bookcopies/<int:pk>/api/metrics/', getattr(views, 'BookCopiesAPIMetricsView').as_view(), name='bookcopies_api_metrics'),
    path('bookcopies/dashboard/', getattr(views, 'BookCopiesDashboardView', getattr(views, 'BookCopiesListView')).as_view(), name='bookcopies_dashboard'),
    path('bookcopies/analytics/', getattr(views, 'BookCopiesAnalyticsView', getattr(views, 'BookCopiesListView')).as_view(), name='bookcopies_analytics'),
]

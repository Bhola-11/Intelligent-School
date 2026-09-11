"""URL Routing for EduFlow Institutional Circulars & Acknowledgments (Circulars)."""
from django.urls import path
try:
    from . import views_circulars as views
except ImportError:
    from . import views

app_name = 'communication'

urlpatterns = [
    path('circulars/', getattr(views, 'CircularsListView').as_view(), name='circulars_list'),
    path('circulars/create/', getattr(views, 'CircularsCreateView').as_view(), name='circulars_create'),
    path('circulars/<int:pk>/', getattr(views, 'CircularsDetailView').as_view(), name='circulars_detail'),
    path('circulars/<int:pk>/edit/', getattr(views, 'CircularsUpdateView').as_view(), name='circulars_edit'),
    path('circulars/<int:pk>/delete/', getattr(views, 'CircularsDeleteView').as_view(), name='circulars_delete'),
    path('circulars/<int:master_pk>/add-item/', getattr(views, 'CircularsItemCreateView').as_view(), name='circulars_add_item'),
    path('circulars/<int:master_pk>/allocate/', getattr(views, 'CircularsAllocationCreateView').as_view(), name='circulars_allocate'),
    path('circulars/bulk-update/', getattr(views, 'CircularsBulkStatusUpdateView').as_view(), name='circulars_bulk_update'),
    path('circulars/export/csv/', getattr(views, 'CircularsExportCSVView').as_view(), name='circulars_export_csv'),
    path('circulars/export/json/', getattr(views, 'CircularsExportJSONView').as_view(), name='circulars_export_json'),
    path('circulars/api/list/', getattr(views, 'CircularsAPIListView').as_view(), name='circulars_api_list'),
    path('circulars/<int:pk>/api/metrics/', getattr(views, 'CircularsAPIMetricsView').as_view(), name='circulars_api_metrics'),
    path('circulars/dashboard/', getattr(views, 'CircularsDashboardView', getattr(views, 'CircularsListView')).as_view(), name='circulars_dashboard'),
    path('circulars/analytics/', getattr(views, 'CircularsAnalyticsView', getattr(views, 'CircularsListView')).as_view(), name='circulars_analytics'),
]

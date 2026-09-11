"""URL Routing for EduFlow Transport Routes, Stops & Timings (Routes)."""
from django.urls import path
try:
    from . import views_routes as views
except ImportError:
    from . import views

app_name = 'transport'

urlpatterns = [
    path('routes/', getattr(views, 'RoutesListView').as_view(), name='routes_list'),
    path('routes/create/', getattr(views, 'RoutesCreateView').as_view(), name='routes_create'),
    path('routes/<int:pk>/', getattr(views, 'RoutesDetailView').as_view(), name='routes_detail'),
    path('routes/<int:pk>/edit/', getattr(views, 'RoutesUpdateView').as_view(), name='routes_edit'),
    path('routes/<int:pk>/delete/', getattr(views, 'RoutesDeleteView').as_view(), name='routes_delete'),
    path('routes/<int:master_pk>/add-item/', getattr(views, 'RoutesItemCreateView').as_view(), name='routes_add_item'),
    path('routes/<int:master_pk>/allocate/', getattr(views, 'RoutesAllocationCreateView').as_view(), name='routes_allocate'),
    path('routes/bulk-update/', getattr(views, 'RoutesBulkStatusUpdateView').as_view(), name='routes_bulk_update'),
    path('routes/export/csv/', getattr(views, 'RoutesExportCSVView').as_view(), name='routes_export_csv'),
    path('routes/export/json/', getattr(views, 'RoutesExportJSONView').as_view(), name='routes_export_json'),
    path('routes/api/list/', getattr(views, 'RoutesAPIListView').as_view(), name='routes_api_list'),
    path('routes/<int:pk>/api/metrics/', getattr(views, 'RoutesAPIMetricsView').as_view(), name='routes_api_metrics'),
    path('routes/dashboard/', getattr(views, 'RoutesDashboardView', getattr(views, 'RoutesListView')).as_view(), name='routes_dashboard'),
    path('routes/analytics/', getattr(views, 'RoutesAnalyticsView', getattr(views, 'RoutesListView')).as_view(), name='routes_analytics'),
]

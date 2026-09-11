"""URL Routing for EduFlow Vehicles, Drivers & Fleet Maintenance (Vehicles)."""
from django.urls import path
try:
    from . import views_vehicles as views
except ImportError:
    from . import views

app_name = 'transport'

urlpatterns = [
    path('vehicles/', getattr(views, 'VehiclesListView').as_view(), name='vehicles_list'),
    path('vehicles/create/', getattr(views, 'VehiclesCreateView').as_view(), name='vehicles_create'),
    path('vehicles/<int:pk>/', getattr(views, 'VehiclesDetailView').as_view(), name='vehicles_detail'),
    path('vehicles/<int:pk>/edit/', getattr(views, 'VehiclesUpdateView').as_view(), name='vehicles_edit'),
    path('vehicles/<int:pk>/delete/', getattr(views, 'VehiclesDeleteView').as_view(), name='vehicles_delete'),
    path('vehicles/<int:master_pk>/add-item/', getattr(views, 'VehiclesItemCreateView').as_view(), name='vehicles_add_item'),
    path('vehicles/<int:master_pk>/allocate/', getattr(views, 'VehiclesAllocationCreateView').as_view(), name='vehicles_allocate'),
    path('vehicles/bulk-update/', getattr(views, 'VehiclesBulkStatusUpdateView').as_view(), name='vehicles_bulk_update'),
    path('vehicles/export/csv/', getattr(views, 'VehiclesExportCSVView').as_view(), name='vehicles_export_csv'),
    path('vehicles/export/json/', getattr(views, 'VehiclesExportJSONView').as_view(), name='vehicles_export_json'),
    path('vehicles/api/list/', getattr(views, 'VehiclesAPIListView').as_view(), name='vehicles_api_list'),
    path('vehicles/<int:pk>/api/metrics/', getattr(views, 'VehiclesAPIMetricsView').as_view(), name='vehicles_api_metrics'),
    path('vehicles/dashboard/', getattr(views, 'VehiclesDashboardView', getattr(views, 'VehiclesListView')).as_view(), name='vehicles_dashboard'),
    path('vehicles/analytics/', getattr(views, 'VehiclesAnalyticsView', getattr(views, 'VehiclesListView')).as_view(), name='vehicles_analytics'),
]

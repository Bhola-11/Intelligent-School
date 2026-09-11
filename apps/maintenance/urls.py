"""URL Routing for EduFlow Maintenance Tickets & Work Orders (MaintenanceTickets)."""
from django.urls import path
try:
    from . import views_maintenancetickets as views
except ImportError:
    from . import views

app_name = 'maintenance'

urlpatterns = [
    path('maintenancetickets/', getattr(views, 'MaintenanceTicketsListView').as_view(), name='maintenancetickets_list'),
    path('maintenancetickets/create/', getattr(views, 'MaintenanceTicketsCreateView').as_view(), name='maintenancetickets_create'),
    path('maintenancetickets/<int:pk>/', getattr(views, 'MaintenanceTicketsDetailView').as_view(), name='maintenancetickets_detail'),
    path('maintenancetickets/<int:pk>/edit/', getattr(views, 'MaintenanceTicketsUpdateView').as_view(), name='maintenancetickets_edit'),
    path('maintenancetickets/<int:pk>/delete/', getattr(views, 'MaintenanceTicketsDeleteView').as_view(), name='maintenancetickets_delete'),
    path('maintenancetickets/<int:master_pk>/add-item/', getattr(views, 'MaintenanceTicketsItemCreateView').as_view(), name='maintenancetickets_add_item'),
    path('maintenancetickets/<int:master_pk>/allocate/', getattr(views, 'MaintenanceTicketsAllocationCreateView').as_view(), name='maintenancetickets_allocate'),
    path('maintenancetickets/bulk-update/', getattr(views, 'MaintenanceTicketsBulkStatusUpdateView').as_view(), name='maintenancetickets_bulk_update'),
    path('maintenancetickets/export/csv/', getattr(views, 'MaintenanceTicketsExportCSVView').as_view(), name='maintenancetickets_export_csv'),
    path('maintenancetickets/export/json/', getattr(views, 'MaintenanceTicketsExportJSONView').as_view(), name='maintenancetickets_export_json'),
    path('maintenancetickets/api/list/', getattr(views, 'MaintenanceTicketsAPIListView').as_view(), name='maintenancetickets_api_list'),
    path('maintenancetickets/<int:pk>/api/metrics/', getattr(views, 'MaintenanceTicketsAPIMetricsView').as_view(), name='maintenancetickets_api_metrics'),
    path('maintenancetickets/dashboard/', getattr(views, 'MaintenanceTicketsDashboardView', getattr(views, 'MaintenanceTicketsListView')).as_view(), name='maintenancetickets_dashboard'),
    path('maintenancetickets/analytics/', getattr(views, 'MaintenanceTicketsAnalyticsView', getattr(views, 'MaintenanceTicketsListView')).as_view(), name='maintenancetickets_analytics'),
]

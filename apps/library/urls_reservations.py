"""URL Routing for EduFlow Book Reservations & Overdue Fines (Reservations)."""
from django.urls import path
try:
    from . import views_reservations as views
except ImportError:
    from . import views

app_name = 'library'

urlpatterns = [
    path('reservations/', getattr(views, 'ReservationsListView').as_view(), name='reservations_list'),
    path('reservations/create/', getattr(views, 'ReservationsCreateView').as_view(), name='reservations_create'),
    path('reservations/<int:pk>/', getattr(views, 'ReservationsDetailView').as_view(), name='reservations_detail'),
    path('reservations/<int:pk>/edit/', getattr(views, 'ReservationsUpdateView').as_view(), name='reservations_edit'),
    path('reservations/<int:pk>/delete/', getattr(views, 'ReservationsDeleteView').as_view(), name='reservations_delete'),
    path('reservations/<int:master_pk>/add-item/', getattr(views, 'ReservationsItemCreateView').as_view(), name='reservations_add_item'),
    path('reservations/<int:master_pk>/allocate/', getattr(views, 'ReservationsAllocationCreateView').as_view(), name='reservations_allocate'),
    path('reservations/bulk-update/', getattr(views, 'ReservationsBulkStatusUpdateView').as_view(), name='reservations_bulk_update'),
    path('reservations/export/csv/', getattr(views, 'ReservationsExportCSVView').as_view(), name='reservations_export_csv'),
    path('reservations/export/json/', getattr(views, 'ReservationsExportJSONView').as_view(), name='reservations_export_json'),
    path('reservations/api/list/', getattr(views, 'ReservationsAPIListView').as_view(), name='reservations_api_list'),
    path('reservations/<int:pk>/api/metrics/', getattr(views, 'ReservationsAPIMetricsView').as_view(), name='reservations_api_metrics'),
    path('reservations/dashboard/', getattr(views, 'ReservationsDashboardView', getattr(views, 'ReservationsListView')).as_view(), name='reservations_dashboard'),
    path('reservations/analytics/', getattr(views, 'ReservationsAnalyticsView', getattr(views, 'ReservationsListView')).as_view(), name='reservations_analytics'),
]

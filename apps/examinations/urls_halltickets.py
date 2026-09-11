"""URL Routing for EduFlow Exam Hall Tickets & Roll Number Generation (HallTickets)."""
from django.urls import path
try:
    from . import views_halltickets as views
except ImportError:
    from . import views

app_name = 'examinations'

urlpatterns = [
    path('halltickets/', getattr(views, 'HallTicketsListView').as_view(), name='halltickets_list'),
    path('halltickets/create/', getattr(views, 'HallTicketsCreateView').as_view(), name='halltickets_create'),
    path('halltickets/<int:pk>/', getattr(views, 'HallTicketsDetailView').as_view(), name='halltickets_detail'),
    path('halltickets/<int:pk>/edit/', getattr(views, 'HallTicketsUpdateView').as_view(), name='halltickets_edit'),
    path('halltickets/<int:pk>/delete/', getattr(views, 'HallTicketsDeleteView').as_view(), name='halltickets_delete'),
    path('halltickets/<int:master_pk>/add-item/', getattr(views, 'HallTicketsItemCreateView').as_view(), name='halltickets_add_item'),
    path('halltickets/<int:master_pk>/allocate/', getattr(views, 'HallTicketsAllocationCreateView').as_view(), name='halltickets_allocate'),
    path('halltickets/bulk-update/', getattr(views, 'HallTicketsBulkStatusUpdateView').as_view(), name='halltickets_bulk_update'),
    path('halltickets/export/csv/', getattr(views, 'HallTicketsExportCSVView').as_view(), name='halltickets_export_csv'),
    path('halltickets/export/json/', getattr(views, 'HallTicketsExportJSONView').as_view(), name='halltickets_export_json'),
    path('halltickets/api/list/', getattr(views, 'HallTicketsAPIListView').as_view(), name='halltickets_api_list'),
    path('halltickets/<int:pk>/api/metrics/', getattr(views, 'HallTicketsAPIMetricsView').as_view(), name='halltickets_api_metrics'),
    path('halltickets/dashboard/', getattr(views, 'HallTicketsDashboardView', getattr(views, 'HallTicketsListView')).as_view(), name='halltickets_dashboard'),
    path('halltickets/analytics/', getattr(views, 'HallTicketsAnalyticsView', getattr(views, 'HallTicketsListView')).as_view(), name='halltickets_analytics'),
]

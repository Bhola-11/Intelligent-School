"""URL Routing for EduFlow Academic Calendar, Terms & Semesters (Calendar)."""
from django.urls import path
try:
    from . import views_calendar as views
except ImportError:
    from . import views

app_name = 'institution'

urlpatterns = [
    path('calendar/', getattr(views, 'CalendarListView').as_view(), name='calendar_list'),
    path('calendar/create/', getattr(views, 'CalendarCreateView').as_view(), name='calendar_create'),
    path('calendar/<int:pk>/', getattr(views, 'CalendarDetailView').as_view(), name='calendar_detail'),
    path('calendar/<int:pk>/edit/', getattr(views, 'CalendarUpdateView').as_view(), name='calendar_edit'),
    path('calendar/<int:pk>/delete/', getattr(views, 'CalendarDeleteView').as_view(), name='calendar_delete'),
    path('calendar/<int:master_pk>/add-item/', getattr(views, 'CalendarItemCreateView').as_view(), name='calendar_add_item'),
    path('calendar/<int:master_pk>/allocate/', getattr(views, 'CalendarAllocationCreateView').as_view(), name='calendar_allocate'),
    path('calendar/bulk-update/', getattr(views, 'CalendarBulkStatusUpdateView').as_view(), name='calendar_bulk_update'),
    path('calendar/export/csv/', getattr(views, 'CalendarExportCSVView').as_view(), name='calendar_export_csv'),
    path('calendar/export/json/', getattr(views, 'CalendarExportJSONView').as_view(), name='calendar_export_json'),
    path('calendar/api/list/', getattr(views, 'CalendarAPIListView').as_view(), name='calendar_api_list'),
    path('calendar/<int:pk>/api/metrics/', getattr(views, 'CalendarAPIMetricsView').as_view(), name='calendar_api_metrics'),
    path('calendar/dashboard/', getattr(views, 'CalendarDashboardView', getattr(views, 'CalendarListView')).as_view(), name='calendar_dashboard'),
    path('calendar/analytics/', getattr(views, 'CalendarAnalyticsView', getattr(views, 'CalendarListView')).as_view(), name='calendar_analytics'),
]

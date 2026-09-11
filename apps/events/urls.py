"""URL Routing for EduFlow Institutional Events & Activity Calendar (EventsCalendar)."""
from django.urls import path
try:
    from . import views_eventscalendar as views
except ImportError:
    from . import views

app_name = 'events'

urlpatterns = [
    path('eventscalendar/', getattr(views, 'EventsCalendarListView').as_view(), name='eventscalendar_list'),
    path('eventscalendar/create/', getattr(views, 'EventsCalendarCreateView').as_view(), name='eventscalendar_create'),
    path('eventscalendar/<int:pk>/', getattr(views, 'EventsCalendarDetailView').as_view(), name='eventscalendar_detail'),
    path('eventscalendar/<int:pk>/edit/', getattr(views, 'EventsCalendarUpdateView').as_view(), name='eventscalendar_edit'),
    path('eventscalendar/<int:pk>/delete/', getattr(views, 'EventsCalendarDeleteView').as_view(), name='eventscalendar_delete'),
    path('eventscalendar/<int:master_pk>/add-item/', getattr(views, 'EventsCalendarItemCreateView').as_view(), name='eventscalendar_add_item'),
    path('eventscalendar/<int:master_pk>/allocate/', getattr(views, 'EventsCalendarAllocationCreateView').as_view(), name='eventscalendar_allocate'),
    path('eventscalendar/bulk-update/', getattr(views, 'EventsCalendarBulkStatusUpdateView').as_view(), name='eventscalendar_bulk_update'),
    path('eventscalendar/export/csv/', getattr(views, 'EventsCalendarExportCSVView').as_view(), name='eventscalendar_export_csv'),
    path('eventscalendar/export/json/', getattr(views, 'EventsCalendarExportJSONView').as_view(), name='eventscalendar_export_json'),
    path('eventscalendar/api/list/', getattr(views, 'EventsCalendarAPIListView').as_view(), name='eventscalendar_api_list'),
    path('eventscalendar/<int:pk>/api/metrics/', getattr(views, 'EventsCalendarAPIMetricsView').as_view(), name='eventscalendar_api_metrics'),
    path('eventscalendar/dashboard/', getattr(views, 'EventsCalendarDashboardView', getattr(views, 'EventsCalendarListView')).as_view(), name='eventscalendar_dashboard'),
    path('eventscalendar/analytics/', getattr(views, 'EventsCalendarAnalyticsView', getattr(views, 'EventsCalendarListView')).as_view(), name='eventscalendar_analytics'),
]

"""URL Routing for EduFlow Timetable Periods & Time Slot Definitions (TimeSlots)."""
from django.urls import path
try:
    from . import views_timeslots as views
except ImportError:
    from . import views

app_name = 'timetable'

urlpatterns = [
    path('timeslots/', getattr(views, 'TimeSlotsListView').as_view(), name='timeslots_list'),
    path('timeslots/create/', getattr(views, 'TimeSlotsCreateView').as_view(), name='timeslots_create'),
    path('timeslots/<int:pk>/', getattr(views, 'TimeSlotsDetailView').as_view(), name='timeslots_detail'),
    path('timeslots/<int:pk>/edit/', getattr(views, 'TimeSlotsUpdateView').as_view(), name='timeslots_edit'),
    path('timeslots/<int:pk>/delete/', getattr(views, 'TimeSlotsDeleteView').as_view(), name='timeslots_delete'),
    path('timeslots/<int:master_pk>/add-item/', getattr(views, 'TimeSlotsItemCreateView').as_view(), name='timeslots_add_item'),
    path('timeslots/<int:master_pk>/allocate/', getattr(views, 'TimeSlotsAllocationCreateView').as_view(), name='timeslots_allocate'),
    path('timeslots/bulk-update/', getattr(views, 'TimeSlotsBulkStatusUpdateView').as_view(), name='timeslots_bulk_update'),
    path('timeslots/export/csv/', getattr(views, 'TimeSlotsExportCSVView').as_view(), name='timeslots_export_csv'),
    path('timeslots/export/json/', getattr(views, 'TimeSlotsExportJSONView').as_view(), name='timeslots_export_json'),
    path('timeslots/api/list/', getattr(views, 'TimeSlotsAPIListView').as_view(), name='timeslots_api_list'),
    path('timeslots/<int:pk>/api/metrics/', getattr(views, 'TimeSlotsAPIMetricsView').as_view(), name='timeslots_api_metrics'),
    path('timeslots/dashboard/', getattr(views, 'TimeSlotsDashboardView', getattr(views, 'TimeSlotsListView')).as_view(), name='timeslots_dashboard'),
    path('timeslots/analytics/', getattr(views, 'TimeSlotsAnalyticsView', getattr(views, 'TimeSlotsListView')).as_view(), name='timeslots_analytics'),
]

"""URL Routing for EduFlow Student Daily Attendance Register (DailyAttendance)."""
from django.urls import path
try:
    from . import views_dailyattendance as views
except ImportError:
    from . import views

app_name = 'attendance'

urlpatterns = [
    path('dailyattendance/', getattr(views, 'DailyAttendanceListView').as_view(), name='dailyattendance_list'),
    path('dailyattendance/create/', getattr(views, 'DailyAttendanceCreateView').as_view(), name='dailyattendance_create'),
    path('dailyattendance/<int:pk>/', getattr(views, 'DailyAttendanceDetailView').as_view(), name='dailyattendance_detail'),
    path('dailyattendance/<int:pk>/edit/', getattr(views, 'DailyAttendanceUpdateView').as_view(), name='dailyattendance_edit'),
    path('dailyattendance/<int:pk>/delete/', getattr(views, 'DailyAttendanceDeleteView').as_view(), name='dailyattendance_delete'),
    path('dailyattendance/<int:master_pk>/add-item/', getattr(views, 'DailyAttendanceItemCreateView').as_view(), name='dailyattendance_add_item'),
    path('dailyattendance/<int:master_pk>/allocate/', getattr(views, 'DailyAttendanceAllocationCreateView').as_view(), name='dailyattendance_allocate'),
    path('dailyattendance/bulk-update/', getattr(views, 'DailyAttendanceBulkStatusUpdateView').as_view(), name='dailyattendance_bulk_update'),
    path('dailyattendance/export/csv/', getattr(views, 'DailyAttendanceExportCSVView').as_view(), name='dailyattendance_export_csv'),
    path('dailyattendance/export/json/', getattr(views, 'DailyAttendanceExportJSONView').as_view(), name='dailyattendance_export_json'),
    path('dailyattendance/api/list/', getattr(views, 'DailyAttendanceAPIListView').as_view(), name='dailyattendance_api_list'),
    path('dailyattendance/<int:pk>/api/metrics/', getattr(views, 'DailyAttendanceAPIMetricsView').as_view(), name='dailyattendance_api_metrics'),
    path('dailyattendance/dashboard/', getattr(views, 'DailyAttendanceDashboardView', getattr(views, 'DailyAttendanceListView')).as_view(), name='dailyattendance_dashboard'),
    path('dailyattendance/analytics/', getattr(views, 'DailyAttendanceAnalyticsView', getattr(views, 'DailyAttendanceListView')).as_view(), name='dailyattendance_analytics'),
]

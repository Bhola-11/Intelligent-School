"""URL Routing for EduFlow Teacher & Staff Attendance Management (StaffAttendance)."""
from django.urls import path
try:
    from . import views_staffattendance as views
except ImportError:
    from . import views

app_name = 'attendance'

urlpatterns = [
    path('staffattendance/', getattr(views, 'StaffAttendanceListView').as_view(), name='staffattendance_list'),
    path('staffattendance/create/', getattr(views, 'StaffAttendanceCreateView').as_view(), name='staffattendance_create'),
    path('staffattendance/<int:pk>/', getattr(views, 'StaffAttendanceDetailView').as_view(), name='staffattendance_detail'),
    path('staffattendance/<int:pk>/edit/', getattr(views, 'StaffAttendanceUpdateView').as_view(), name='staffattendance_edit'),
    path('staffattendance/<int:pk>/delete/', getattr(views, 'StaffAttendanceDeleteView').as_view(), name='staffattendance_delete'),
    path('staffattendance/<int:master_pk>/add-item/', getattr(views, 'StaffAttendanceItemCreateView').as_view(), name='staffattendance_add_item'),
    path('staffattendance/<int:master_pk>/allocate/', getattr(views, 'StaffAttendanceAllocationCreateView').as_view(), name='staffattendance_allocate'),
    path('staffattendance/bulk-update/', getattr(views, 'StaffAttendanceBulkStatusUpdateView').as_view(), name='staffattendance_bulk_update'),
    path('staffattendance/export/csv/', getattr(views, 'StaffAttendanceExportCSVView').as_view(), name='staffattendance_export_csv'),
    path('staffattendance/export/json/', getattr(views, 'StaffAttendanceExportJSONView').as_view(), name='staffattendance_export_json'),
    path('staffattendance/api/list/', getattr(views, 'StaffAttendanceAPIListView').as_view(), name='staffattendance_api_list'),
    path('staffattendance/<int:pk>/api/metrics/', getattr(views, 'StaffAttendanceAPIMetricsView').as_view(), name='staffattendance_api_metrics'),
    path('staffattendance/dashboard/', getattr(views, 'StaffAttendanceDashboardView', getattr(views, 'StaffAttendanceListView')).as_view(), name='staffattendance_dashboard'),
    path('staffattendance/analytics/', getattr(views, 'StaffAttendanceAnalyticsView', getattr(views, 'StaffAttendanceListView')).as_view(), name='staffattendance_analytics'),
]

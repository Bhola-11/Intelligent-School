"""URL Routing for EduFlow Period & Subject-Wise Attendance Tracking (PeriodAttendance)."""
from django.urls import path
try:
    from . import views_periodattendance as views
except ImportError:
    from . import views

app_name = 'attendance'

urlpatterns = [
    path('periodattendance/', getattr(views, 'PeriodAttendanceListView').as_view(), name='periodattendance_list'),
    path('periodattendance/create/', getattr(views, 'PeriodAttendanceCreateView').as_view(), name='periodattendance_create'),
    path('periodattendance/<int:pk>/', getattr(views, 'PeriodAttendanceDetailView').as_view(), name='periodattendance_detail'),
    path('periodattendance/<int:pk>/edit/', getattr(views, 'PeriodAttendanceUpdateView').as_view(), name='periodattendance_edit'),
    path('periodattendance/<int:pk>/delete/', getattr(views, 'PeriodAttendanceDeleteView').as_view(), name='periodattendance_delete'),
    path('periodattendance/<int:master_pk>/add-item/', getattr(views, 'PeriodAttendanceItemCreateView').as_view(), name='periodattendance_add_item'),
    path('periodattendance/<int:master_pk>/allocate/', getattr(views, 'PeriodAttendanceAllocationCreateView').as_view(), name='periodattendance_allocate'),
    path('periodattendance/bulk-update/', getattr(views, 'PeriodAttendanceBulkStatusUpdateView').as_view(), name='periodattendance_bulk_update'),
    path('periodattendance/export/csv/', getattr(views, 'PeriodAttendanceExportCSVView').as_view(), name='periodattendance_export_csv'),
    path('periodattendance/export/json/', getattr(views, 'PeriodAttendanceExportJSONView').as_view(), name='periodattendance_export_json'),
    path('periodattendance/api/list/', getattr(views, 'PeriodAttendanceAPIListView').as_view(), name='periodattendance_api_list'),
    path('periodattendance/<int:pk>/api/metrics/', getattr(views, 'PeriodAttendanceAPIMetricsView').as_view(), name='periodattendance_api_metrics'),
    path('periodattendance/dashboard/', getattr(views, 'PeriodAttendanceDashboardView', getattr(views, 'PeriodAttendanceListView')).as_view(), name='periodattendance_dashboard'),
    path('periodattendance/analytics/', getattr(views, 'PeriodAttendanceAnalyticsView', getattr(views, 'PeriodAttendanceListView')).as_view(), name='periodattendance_analytics'),
]

"""URL Routing for EduFlow Attendance Policies, Alerts & Analytics (AttendanceReports)."""
from django.urls import path
try:
    from . import views_attendancereports as views
except ImportError:
    from . import views

app_name = 'attendance'

urlpatterns = [
    path('attendancereports/', getattr(views, 'AttendanceReportsListView').as_view(), name='attendancereports_list'),
    path('attendancereports/create/', getattr(views, 'AttendanceReportsCreateView').as_view(), name='attendancereports_create'),
    path('attendancereports/<int:pk>/', getattr(views, 'AttendanceReportsDetailView').as_view(), name='attendancereports_detail'),
    path('attendancereports/<int:pk>/edit/', getattr(views, 'AttendanceReportsUpdateView').as_view(), name='attendancereports_edit'),
    path('attendancereports/<int:pk>/delete/', getattr(views, 'AttendanceReportsDeleteView').as_view(), name='attendancereports_delete'),
    path('attendancereports/<int:master_pk>/add-item/', getattr(views, 'AttendanceReportsItemCreateView').as_view(), name='attendancereports_add_item'),
    path('attendancereports/<int:master_pk>/allocate/', getattr(views, 'AttendanceReportsAllocationCreateView').as_view(), name='attendancereports_allocate'),
    path('attendancereports/bulk-update/', getattr(views, 'AttendanceReportsBulkStatusUpdateView').as_view(), name='attendancereports_bulk_update'),
    path('attendancereports/export/csv/', getattr(views, 'AttendanceReportsExportCSVView').as_view(), name='attendancereports_export_csv'),
    path('attendancereports/export/json/', getattr(views, 'AttendanceReportsExportJSONView').as_view(), name='attendancereports_export_json'),
    path('attendancereports/api/list/', getattr(views, 'AttendanceReportsAPIListView').as_view(), name='attendancereports_api_list'),
    path('attendancereports/<int:pk>/api/metrics/', getattr(views, 'AttendanceReportsAPIMetricsView').as_view(), name='attendancereports_api_metrics'),
    path('attendancereports/dashboard/', getattr(views, 'AttendanceReportsDashboardView', getattr(views, 'AttendanceReportsListView')).as_view(), name='attendancereports_dashboard'),
    path('attendancereports/analytics/', getattr(views, 'AttendanceReportsAnalyticsView', getattr(views, 'AttendanceReportsListView')).as_view(), name='attendancereports_analytics'),
]

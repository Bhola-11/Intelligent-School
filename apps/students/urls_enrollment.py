"""URL Routing for EduFlow Student Enrollment & Academic History (Enrollment)."""
from django.urls import path
try:
    from . import views_enrollment as views
except ImportError:
    from . import views

app_name = 'students'

urlpatterns = [
    path('enrollment/', getattr(views, 'EnrollmentListView').as_view(), name='enrollment_list'),
    path('enrollment/create/', getattr(views, 'EnrollmentCreateView').as_view(), name='enrollment_create'),
    path('enrollment/<int:pk>/', getattr(views, 'EnrollmentDetailView').as_view(), name='enrollment_detail'),
    path('enrollment/<int:pk>/edit/', getattr(views, 'EnrollmentUpdateView').as_view(), name='enrollment_edit'),
    path('enrollment/<int:pk>/delete/', getattr(views, 'EnrollmentDeleteView').as_view(), name='enrollment_delete'),
    path('enrollment/<int:master_pk>/add-item/', getattr(views, 'EnrollmentItemCreateView').as_view(), name='enrollment_add_item'),
    path('enrollment/<int:master_pk>/allocate/', getattr(views, 'EnrollmentAllocationCreateView').as_view(), name='enrollment_allocate'),
    path('enrollment/bulk-update/', getattr(views, 'EnrollmentBulkStatusUpdateView').as_view(), name='enrollment_bulk_update'),
    path('enrollment/export/csv/', getattr(views, 'EnrollmentExportCSVView').as_view(), name='enrollment_export_csv'),
    path('enrollment/export/json/', getattr(views, 'EnrollmentExportJSONView').as_view(), name='enrollment_export_json'),
    path('enrollment/api/list/', getattr(views, 'EnrollmentAPIListView').as_view(), name='enrollment_api_list'),
    path('enrollment/<int:pk>/api/metrics/', getattr(views, 'EnrollmentAPIMetricsView').as_view(), name='enrollment_api_metrics'),
    path('enrollment/dashboard/', getattr(views, 'EnrollmentDashboardView', getattr(views, 'EnrollmentListView')).as_view(), name='enrollment_dashboard'),
    path('enrollment/analytics/', getattr(views, 'EnrollmentAnalyticsView', getattr(views, 'EnrollmentListView')).as_view(), name='enrollment_analytics'),
]

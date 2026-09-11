"""URL Routing for EduFlow Student Assignment Submissions Desk (Submissions)."""
from django.urls import path
try:
    from . import views_submissions as views
except ImportError:
    from . import views

app_name = 'assignments'

urlpatterns = [
    path('submissions/', getattr(views, 'SubmissionsListView').as_view(), name='submissions_list'),
    path('submissions/create/', getattr(views, 'SubmissionsCreateView').as_view(), name='submissions_create'),
    path('submissions/<int:pk>/', getattr(views, 'SubmissionsDetailView').as_view(), name='submissions_detail'),
    path('submissions/<int:pk>/edit/', getattr(views, 'SubmissionsUpdateView').as_view(), name='submissions_edit'),
    path('submissions/<int:pk>/delete/', getattr(views, 'SubmissionsDeleteView').as_view(), name='submissions_delete'),
    path('submissions/<int:master_pk>/add-item/', getattr(views, 'SubmissionsItemCreateView').as_view(), name='submissions_add_item'),
    path('submissions/<int:master_pk>/allocate/', getattr(views, 'SubmissionsAllocationCreateView').as_view(), name='submissions_allocate'),
    path('submissions/bulk-update/', getattr(views, 'SubmissionsBulkStatusUpdateView').as_view(), name='submissions_bulk_update'),
    path('submissions/export/csv/', getattr(views, 'SubmissionsExportCSVView').as_view(), name='submissions_export_csv'),
    path('submissions/export/json/', getattr(views, 'SubmissionsExportJSONView').as_view(), name='submissions_export_json'),
    path('submissions/api/list/', getattr(views, 'SubmissionsAPIListView').as_view(), name='submissions_api_list'),
    path('submissions/<int:pk>/api/metrics/', getattr(views, 'SubmissionsAPIMetricsView').as_view(), name='submissions_api_metrics'),
    path('submissions/dashboard/', getattr(views, 'SubmissionsDashboardView', getattr(views, 'SubmissionsListView')).as_view(), name='submissions_dashboard'),
    path('submissions/analytics/', getattr(views, 'SubmissionsAnalyticsView', getattr(views, 'SubmissionsListView')).as_view(), name='submissions_analytics'),
]

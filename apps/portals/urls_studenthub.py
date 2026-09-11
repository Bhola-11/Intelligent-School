"""URL Routing for EduFlow Student Learning Hub & Portal (StudentHub)."""
from django.urls import path
try:
    from . import views_studenthub as views
except ImportError:
    from . import views

app_name = 'portals'

urlpatterns = [
    path('studenthub/', getattr(views, 'StudentHubListView').as_view(), name='studenthub_list'),
    path('studenthub/create/', getattr(views, 'StudentHubCreateView').as_view(), name='studenthub_create'),
    path('studenthub/<int:pk>/', getattr(views, 'StudentHubDetailView').as_view(), name='studenthub_detail'),
    path('studenthub/<int:pk>/edit/', getattr(views, 'StudentHubUpdateView').as_view(), name='studenthub_edit'),
    path('studenthub/<int:pk>/delete/', getattr(views, 'StudentHubDeleteView').as_view(), name='studenthub_delete'),
    path('studenthub/<int:master_pk>/add-item/', getattr(views, 'StudentHubItemCreateView').as_view(), name='studenthub_add_item'),
    path('studenthub/<int:master_pk>/allocate/', getattr(views, 'StudentHubAllocationCreateView').as_view(), name='studenthub_allocate'),
    path('studenthub/bulk-update/', getattr(views, 'StudentHubBulkStatusUpdateView').as_view(), name='studenthub_bulk_update'),
    path('studenthub/export/csv/', getattr(views, 'StudentHubExportCSVView').as_view(), name='studenthub_export_csv'),
    path('studenthub/export/json/', getattr(views, 'StudentHubExportJSONView').as_view(), name='studenthub_export_json'),
    path('studenthub/api/list/', getattr(views, 'StudentHubAPIListView').as_view(), name='studenthub_api_list'),
    path('studenthub/<int:pk>/api/metrics/', getattr(views, 'StudentHubAPIMetricsView').as_view(), name='studenthub_api_metrics'),
    path('studenthub/dashboard/', getattr(views, 'StudentHubDashboardView', getattr(views, 'StudentHubListView')).as_view(), name='studenthub_dashboard'),
    path('studenthub/analytics/', getattr(views, 'StudentHubAnalyticsView', getattr(views, 'StudentHubListView')).as_view(), name='studenthub_analytics'),
]

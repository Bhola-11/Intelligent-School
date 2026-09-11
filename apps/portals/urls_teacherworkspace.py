"""URL Routing for EduFlow Teacher Workspace & Daily Register (TeacherWorkspace)."""
from django.urls import path
try:
    from . import views_teacherworkspace as views
except ImportError:
    from . import views

app_name = 'portals'

urlpatterns = [
    path('teacherworkspace/', getattr(views, 'TeacherWorkspaceListView').as_view(), name='teacherworkspace_list'),
    path('teacherworkspace/create/', getattr(views, 'TeacherWorkspaceCreateView').as_view(), name='teacherworkspace_create'),
    path('teacherworkspace/<int:pk>/', getattr(views, 'TeacherWorkspaceDetailView').as_view(), name='teacherworkspace_detail'),
    path('teacherworkspace/<int:pk>/edit/', getattr(views, 'TeacherWorkspaceUpdateView').as_view(), name='teacherworkspace_edit'),
    path('teacherworkspace/<int:pk>/delete/', getattr(views, 'TeacherWorkspaceDeleteView').as_view(), name='teacherworkspace_delete'),
    path('teacherworkspace/<int:master_pk>/add-item/', getattr(views, 'TeacherWorkspaceItemCreateView').as_view(), name='teacherworkspace_add_item'),
    path('teacherworkspace/<int:master_pk>/allocate/', getattr(views, 'TeacherWorkspaceAllocationCreateView').as_view(), name='teacherworkspace_allocate'),
    path('teacherworkspace/bulk-update/', getattr(views, 'TeacherWorkspaceBulkStatusUpdateView').as_view(), name='teacherworkspace_bulk_update'),
    path('teacherworkspace/export/csv/', getattr(views, 'TeacherWorkspaceExportCSVView').as_view(), name='teacherworkspace_export_csv'),
    path('teacherworkspace/export/json/', getattr(views, 'TeacherWorkspaceExportJSONView').as_view(), name='teacherworkspace_export_json'),
    path('teacherworkspace/api/list/', getattr(views, 'TeacherWorkspaceAPIListView').as_view(), name='teacherworkspace_api_list'),
    path('teacherworkspace/<int:pk>/api/metrics/', getattr(views, 'TeacherWorkspaceAPIMetricsView').as_view(), name='teacherworkspace_api_metrics'),
    path('teacherworkspace/dashboard/', getattr(views, 'TeacherWorkspaceDashboardView', getattr(views, 'TeacherWorkspaceListView')).as_view(), name='teacherworkspace_dashboard'),
    path('teacherworkspace/analytics/', getattr(views, 'TeacherWorkspaceAnalyticsView', getattr(views, 'TeacherWorkspaceListView')).as_view(), name='teacherworkspace_analytics'),
]

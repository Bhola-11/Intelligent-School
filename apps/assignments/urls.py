"""URL Routing for EduFlow Assignment & Homework Management (Assignments)."""
from django.urls import path
try:
    from . import views_assignments as views
except ImportError:
    from . import views

app_name = 'assignments'

urlpatterns = [
    path('assignments/', getattr(views, 'AssignmentsListView').as_view(), name='assignments_list'),
    path('assignments/create/', getattr(views, 'AssignmentsCreateView').as_view(), name='assignments_create'),
    path('assignments/<int:pk>/', getattr(views, 'AssignmentsDetailView').as_view(), name='assignments_detail'),
    path('assignments/<int:pk>/edit/', getattr(views, 'AssignmentsUpdateView').as_view(), name='assignments_edit'),
    path('assignments/<int:pk>/delete/', getattr(views, 'AssignmentsDeleteView').as_view(), name='assignments_delete'),
    path('assignments/<int:master_pk>/add-item/', getattr(views, 'AssignmentsItemCreateView').as_view(), name='assignments_add_item'),
    path('assignments/<int:master_pk>/allocate/', getattr(views, 'AssignmentsAllocationCreateView').as_view(), name='assignments_allocate'),
    path('assignments/bulk-update/', getattr(views, 'AssignmentsBulkStatusUpdateView').as_view(), name='assignments_bulk_update'),
    path('assignments/export/csv/', getattr(views, 'AssignmentsExportCSVView').as_view(), name='assignments_export_csv'),
    path('assignments/export/json/', getattr(views, 'AssignmentsExportJSONView').as_view(), name='assignments_export_json'),
    path('assignments/api/list/', getattr(views, 'AssignmentsAPIListView').as_view(), name='assignments_api_list'),
    path('assignments/<int:pk>/api/metrics/', getattr(views, 'AssignmentsAPIMetricsView').as_view(), name='assignments_api_metrics'),
    path('assignments/dashboard/', getattr(views, 'AssignmentsDashboardView', getattr(views, 'AssignmentsListView')).as_view(), name='assignments_dashboard'),
    path('assignments/analytics/', getattr(views, 'AssignmentsAnalyticsView', getattr(views, 'AssignmentsListView')).as_view(), name='assignments_analytics'),
]

"""URL Routing for EduFlow Academic Departments & Faculties (Departments)."""
from django.urls import path
try:
    from . import views_departments as views
except ImportError:
    from . import views

app_name = 'institution'

urlpatterns = [
    path('departments/', getattr(views, 'DepartmentsListView').as_view(), name='departments_list'),
    path('departments/create/', getattr(views, 'DepartmentsCreateView').as_view(), name='departments_create'),
    path('departments/<int:pk>/', getattr(views, 'DepartmentsDetailView').as_view(), name='departments_detail'),
    path('departments/<int:pk>/edit/', getattr(views, 'DepartmentsUpdateView').as_view(), name='departments_edit'),
    path('departments/<int:pk>/delete/', getattr(views, 'DepartmentsDeleteView').as_view(), name='departments_delete'),
    path('departments/<int:master_pk>/add-item/', getattr(views, 'DepartmentsItemCreateView').as_view(), name='departments_add_item'),
    path('departments/<int:master_pk>/allocate/', getattr(views, 'DepartmentsAllocationCreateView').as_view(), name='departments_allocate'),
    path('departments/bulk-update/', getattr(views, 'DepartmentsBulkStatusUpdateView').as_view(), name='departments_bulk_update'),
    path('departments/export/csv/', getattr(views, 'DepartmentsExportCSVView').as_view(), name='departments_export_csv'),
    path('departments/export/json/', getattr(views, 'DepartmentsExportJSONView').as_view(), name='departments_export_json'),
    path('departments/api/list/', getattr(views, 'DepartmentsAPIListView').as_view(), name='departments_api_list'),
    path('departments/<int:pk>/api/metrics/', getattr(views, 'DepartmentsAPIMetricsView').as_view(), name='departments_api_metrics'),
    path('departments/dashboard/', getattr(views, 'DepartmentsDashboardView', getattr(views, 'DepartmentsListView')).as_view(), name='departments_dashboard'),
    path('departments/analytics/', getattr(views, 'DepartmentsAnalyticsView', getattr(views, 'DepartmentsListView')).as_view(), name='departments_analytics'),
]

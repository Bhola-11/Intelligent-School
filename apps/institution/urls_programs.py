"""URL Routing for EduFlow Degree Programs & Course Catalog (Programs)."""
from django.urls import path
try:
    from . import views_programs as views
except ImportError:
    from . import views

app_name = 'institution'

urlpatterns = [
    path('programs/', getattr(views, 'ProgramsListView').as_view(), name='programs_list'),
    path('programs/create/', getattr(views, 'ProgramsCreateView').as_view(), name='programs_create'),
    path('programs/<int:pk>/', getattr(views, 'ProgramsDetailView').as_view(), name='programs_detail'),
    path('programs/<int:pk>/edit/', getattr(views, 'ProgramsUpdateView').as_view(), name='programs_edit'),
    path('programs/<int:pk>/delete/', getattr(views, 'ProgramsDeleteView').as_view(), name='programs_delete'),
    path('programs/<int:master_pk>/add-item/', getattr(views, 'ProgramsItemCreateView').as_view(), name='programs_add_item'),
    path('programs/<int:master_pk>/allocate/', getattr(views, 'ProgramsAllocationCreateView').as_view(), name='programs_allocate'),
    path('programs/bulk-update/', getattr(views, 'ProgramsBulkStatusUpdateView').as_view(), name='programs_bulk_update'),
    path('programs/export/csv/', getattr(views, 'ProgramsExportCSVView').as_view(), name='programs_export_csv'),
    path('programs/export/json/', getattr(views, 'ProgramsExportJSONView').as_view(), name='programs_export_json'),
    path('programs/api/list/', getattr(views, 'ProgramsAPIListView').as_view(), name='programs_api_list'),
    path('programs/<int:pk>/api/metrics/', getattr(views, 'ProgramsAPIMetricsView').as_view(), name='programs_api_metrics'),
    path('programs/dashboard/', getattr(views, 'ProgramsDashboardView', getattr(views, 'ProgramsListView')).as_view(), name='programs_dashboard'),
    path('programs/analytics/', getattr(views, 'ProgramsAnalyticsView', getattr(views, 'ProgramsListView')).as_view(), name='programs_analytics'),
]

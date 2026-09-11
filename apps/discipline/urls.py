"""URL Routing for EduFlow Disciplinary Incidents & Case Management (DisciplineCases)."""
from django.urls import path
try:
    from . import views_disciplinecases as views
except ImportError:
    from . import views

app_name = 'discipline'

urlpatterns = [
    path('disciplinecases/', getattr(views, 'DisciplineCasesListView').as_view(), name='disciplinecases_list'),
    path('disciplinecases/create/', getattr(views, 'DisciplineCasesCreateView').as_view(), name='disciplinecases_create'),
    path('disciplinecases/<int:pk>/', getattr(views, 'DisciplineCasesDetailView').as_view(), name='disciplinecases_detail'),
    path('disciplinecases/<int:pk>/edit/', getattr(views, 'DisciplineCasesUpdateView').as_view(), name='disciplinecases_edit'),
    path('disciplinecases/<int:pk>/delete/', getattr(views, 'DisciplineCasesDeleteView').as_view(), name='disciplinecases_delete'),
    path('disciplinecases/<int:master_pk>/add-item/', getattr(views, 'DisciplineCasesItemCreateView').as_view(), name='disciplinecases_add_item'),
    path('disciplinecases/<int:master_pk>/allocate/', getattr(views, 'DisciplineCasesAllocationCreateView').as_view(), name='disciplinecases_allocate'),
    path('disciplinecases/bulk-update/', getattr(views, 'DisciplineCasesBulkStatusUpdateView').as_view(), name='disciplinecases_bulk_update'),
    path('disciplinecases/export/csv/', getattr(views, 'DisciplineCasesExportCSVView').as_view(), name='disciplinecases_export_csv'),
    path('disciplinecases/export/json/', getattr(views, 'DisciplineCasesExportJSONView').as_view(), name='disciplinecases_export_json'),
    path('disciplinecases/api/list/', getattr(views, 'DisciplineCasesAPIListView').as_view(), name='disciplinecases_api_list'),
    path('disciplinecases/<int:pk>/api/metrics/', getattr(views, 'DisciplineCasesAPIMetricsView').as_view(), name='disciplinecases_api_metrics'),
    path('disciplinecases/dashboard/', getattr(views, 'DisciplineCasesDashboardView', getattr(views, 'DisciplineCasesListView')).as_view(), name='disciplinecases_dashboard'),
    path('disciplinecases/analytics/', getattr(views, 'DisciplineCasesAnalyticsView', getattr(views, 'DisciplineCasesListView')).as_view(), name='disciplinecases_analytics'),
]

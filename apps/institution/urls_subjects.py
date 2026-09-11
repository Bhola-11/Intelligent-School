"""URL Routing for EduFlow Subjects, Syllabi & Credit Hours (Subjects)."""
from django.urls import path
try:
    from . import views_subjects as views
except ImportError:
    from . import views

app_name = 'institution'

urlpatterns = [
    path('subjects/', getattr(views, 'SubjectsListView').as_view(), name='subjects_list'),
    path('subjects/create/', getattr(views, 'SubjectsCreateView').as_view(), name='subjects_create'),
    path('subjects/<int:pk>/', getattr(views, 'SubjectsDetailView').as_view(), name='subjects_detail'),
    path('subjects/<int:pk>/edit/', getattr(views, 'SubjectsUpdateView').as_view(), name='subjects_edit'),
    path('subjects/<int:pk>/delete/', getattr(views, 'SubjectsDeleteView').as_view(), name='subjects_delete'),
    path('subjects/<int:master_pk>/add-item/', getattr(views, 'SubjectsItemCreateView').as_view(), name='subjects_add_item'),
    path('subjects/<int:master_pk>/allocate/', getattr(views, 'SubjectsAllocationCreateView').as_view(), name='subjects_allocate'),
    path('subjects/bulk-update/', getattr(views, 'SubjectsBulkStatusUpdateView').as_view(), name='subjects_bulk_update'),
    path('subjects/export/csv/', getattr(views, 'SubjectsExportCSVView').as_view(), name='subjects_export_csv'),
    path('subjects/export/json/', getattr(views, 'SubjectsExportJSONView').as_view(), name='subjects_export_json'),
    path('subjects/api/list/', getattr(views, 'SubjectsAPIListView').as_view(), name='subjects_api_list'),
    path('subjects/<int:pk>/api/metrics/', getattr(views, 'SubjectsAPIMetricsView').as_view(), name='subjects_api_metrics'),
    path('subjects/dashboard/', getattr(views, 'SubjectsDashboardView', getattr(views, 'SubjectsListView')).as_view(), name='subjects_dashboard'),
    path('subjects/analytics/', getattr(views, 'SubjectsAnalyticsView', getattr(views, 'SubjectsListView')).as_view(), name='subjects_analytics'),
]

"""URL Routing for EduFlow Academic Curriculum & Syllabus Topics (Curriculum)."""
from django.urls import path
try:
    from . import views_curriculum as views
except ImportError:
    from . import views

app_name = 'academics'

urlpatterns = [
    path('curriculum/', getattr(views, 'CurriculumListView').as_view(), name='curriculum_list'),
    path('curriculum/create/', getattr(views, 'CurriculumCreateView').as_view(), name='curriculum_create'),
    path('curriculum/<int:pk>/', getattr(views, 'CurriculumDetailView').as_view(), name='curriculum_detail'),
    path('curriculum/<int:pk>/edit/', getattr(views, 'CurriculumUpdateView').as_view(), name='curriculum_edit'),
    path('curriculum/<int:pk>/delete/', getattr(views, 'CurriculumDeleteView').as_view(), name='curriculum_delete'),
    path('curriculum/<int:master_pk>/add-item/', getattr(views, 'CurriculumItemCreateView').as_view(), name='curriculum_add_item'),
    path('curriculum/<int:master_pk>/allocate/', getattr(views, 'CurriculumAllocationCreateView').as_view(), name='curriculum_allocate'),
    path('curriculum/bulk-update/', getattr(views, 'CurriculumBulkStatusUpdateView').as_view(), name='curriculum_bulk_update'),
    path('curriculum/export/csv/', getattr(views, 'CurriculumExportCSVView').as_view(), name='curriculum_export_csv'),
    path('curriculum/export/json/', getattr(views, 'CurriculumExportJSONView').as_view(), name='curriculum_export_json'),
    path('curriculum/api/list/', getattr(views, 'CurriculumAPIListView').as_view(), name='curriculum_api_list'),
    path('curriculum/<int:pk>/api/metrics/', getattr(views, 'CurriculumAPIMetricsView').as_view(), name='curriculum_api_metrics'),
    path('curriculum/dashboard/', getattr(views, 'CurriculumDashboardView', getattr(views, 'CurriculumListView')).as_view(), name='curriculum_dashboard'),
    path('curriculum/analytics/', getattr(views, 'CurriculumAnalyticsView', getattr(views, 'CurriculumListView')).as_view(), name='curriculum_analytics'),
]

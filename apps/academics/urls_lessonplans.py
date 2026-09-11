"""URL Routing for EduFlow Lesson Plans & Daily Teaching Logs (LessonPlans)."""
from django.urls import path
try:
    from . import views_lessonplans as views
except ImportError:
    from . import views

app_name = 'academics'

urlpatterns = [
    path('lessonplans/', getattr(views, 'LessonPlansListView').as_view(), name='lessonplans_list'),
    path('lessonplans/create/', getattr(views, 'LessonPlansCreateView').as_view(), name='lessonplans_create'),
    path('lessonplans/<int:pk>/', getattr(views, 'LessonPlansDetailView').as_view(), name='lessonplans_detail'),
    path('lessonplans/<int:pk>/edit/', getattr(views, 'LessonPlansUpdateView').as_view(), name='lessonplans_edit'),
    path('lessonplans/<int:pk>/delete/', getattr(views, 'LessonPlansDeleteView').as_view(), name='lessonplans_delete'),
    path('lessonplans/<int:master_pk>/add-item/', getattr(views, 'LessonPlansItemCreateView').as_view(), name='lessonplans_add_item'),
    path('lessonplans/<int:master_pk>/allocate/', getattr(views, 'LessonPlansAllocationCreateView').as_view(), name='lessonplans_allocate'),
    path('lessonplans/bulk-update/', getattr(views, 'LessonPlansBulkStatusUpdateView').as_view(), name='lessonplans_bulk_update'),
    path('lessonplans/export/csv/', getattr(views, 'LessonPlansExportCSVView').as_view(), name='lessonplans_export_csv'),
    path('lessonplans/export/json/', getattr(views, 'LessonPlansExportJSONView').as_view(), name='lessonplans_export_json'),
    path('lessonplans/api/list/', getattr(views, 'LessonPlansAPIListView').as_view(), name='lessonplans_api_list'),
    path('lessonplans/<int:pk>/api/metrics/', getattr(views, 'LessonPlansAPIMetricsView').as_view(), name='lessonplans_api_metrics'),
    path('lessonplans/dashboard/', getattr(views, 'LessonPlansDashboardView', getattr(views, 'LessonPlansListView')).as_view(), name='lessonplans_dashboard'),
    path('lessonplans/analytics/', getattr(views, 'LessonPlansAnalyticsView', getattr(views, 'LessonPlansListView')).as_view(), name='lessonplans_analytics'),
]

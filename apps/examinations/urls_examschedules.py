"""URL Routing for EduFlow Exam Schedules & Timetables (ExamSchedules)."""
from django.urls import path
try:
    from . import views_examschedules as views
except ImportError:
    from . import views

app_name = 'examinations'

urlpatterns = [
    path('examschedules/', getattr(views, 'ExamSchedulesListView').as_view(), name='examschedules_list'),
    path('examschedules/create/', getattr(views, 'ExamSchedulesCreateView').as_view(), name='examschedules_create'),
    path('examschedules/<int:pk>/', getattr(views, 'ExamSchedulesDetailView').as_view(), name='examschedules_detail'),
    path('examschedules/<int:pk>/edit/', getattr(views, 'ExamSchedulesUpdateView').as_view(), name='examschedules_edit'),
    path('examschedules/<int:pk>/delete/', getattr(views, 'ExamSchedulesDeleteView').as_view(), name='examschedules_delete'),
    path('examschedules/<int:master_pk>/add-item/', getattr(views, 'ExamSchedulesItemCreateView').as_view(), name='examschedules_add_item'),
    path('examschedules/<int:master_pk>/allocate/', getattr(views, 'ExamSchedulesAllocationCreateView').as_view(), name='examschedules_allocate'),
    path('examschedules/bulk-update/', getattr(views, 'ExamSchedulesBulkStatusUpdateView').as_view(), name='examschedules_bulk_update'),
    path('examschedules/export/csv/', getattr(views, 'ExamSchedulesExportCSVView').as_view(), name='examschedules_export_csv'),
    path('examschedules/export/json/', getattr(views, 'ExamSchedulesExportJSONView').as_view(), name='examschedules_export_json'),
    path('examschedules/api/list/', getattr(views, 'ExamSchedulesAPIListView').as_view(), name='examschedules_api_list'),
    path('examschedules/<int:pk>/api/metrics/', getattr(views, 'ExamSchedulesAPIMetricsView').as_view(), name='examschedules_api_metrics'),
    path('examschedules/dashboard/', getattr(views, 'ExamSchedulesDashboardView', getattr(views, 'ExamSchedulesListView')).as_view(), name='examschedules_dashboard'),
    path('examschedules/analytics/', getattr(views, 'ExamSchedulesAnalyticsView', getattr(views, 'ExamSchedulesListView')).as_view(), name='examschedules_analytics'),
]

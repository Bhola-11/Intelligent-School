"""URL Routing for EduFlow Examination Sessions & Exam Types (ExamSessions)."""
from django.urls import path
try:
    from . import views_examsessions as views
except ImportError:
    from . import views

app_name = 'examinations'

urlpatterns = [
    path('examsessions/', getattr(views, 'ExamSessionsListView').as_view(), name='examsessions_list'),
    path('examsessions/create/', getattr(views, 'ExamSessionsCreateView').as_view(), name='examsessions_create'),
    path('examsessions/<int:pk>/', getattr(views, 'ExamSessionsDetailView').as_view(), name='examsessions_detail'),
    path('examsessions/<int:pk>/edit/', getattr(views, 'ExamSessionsUpdateView').as_view(), name='examsessions_edit'),
    path('examsessions/<int:pk>/delete/', getattr(views, 'ExamSessionsDeleteView').as_view(), name='examsessions_delete'),
    path('examsessions/<int:master_pk>/add-item/', getattr(views, 'ExamSessionsItemCreateView').as_view(), name='examsessions_add_item'),
    path('examsessions/<int:master_pk>/allocate/', getattr(views, 'ExamSessionsAllocationCreateView').as_view(), name='examsessions_allocate'),
    path('examsessions/bulk-update/', getattr(views, 'ExamSessionsBulkStatusUpdateView').as_view(), name='examsessions_bulk_update'),
    path('examsessions/export/csv/', getattr(views, 'ExamSessionsExportCSVView').as_view(), name='examsessions_export_csv'),
    path('examsessions/export/json/', getattr(views, 'ExamSessionsExportJSONView').as_view(), name='examsessions_export_json'),
    path('examsessions/api/list/', getattr(views, 'ExamSessionsAPIListView').as_view(), name='examsessions_api_list'),
    path('examsessions/<int:pk>/api/metrics/', getattr(views, 'ExamSessionsAPIMetricsView').as_view(), name='examsessions_api_metrics'),
    path('examsessions/dashboard/', getattr(views, 'ExamSessionsDashboardView', getattr(views, 'ExamSessionsListView')).as_view(), name='examsessions_dashboard'),
    path('examsessions/analytics/', getattr(views, 'ExamSessionsAnalyticsView', getattr(views, 'ExamSessionsListView')).as_view(), name='examsessions_analytics'),
]

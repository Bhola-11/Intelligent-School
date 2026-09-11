"""URL Routing for EduFlow Admissions Entrance Exams & Interviews (EntranceExam)."""
from django.urls import path
try:
    from . import views_entranceexam as views
except ImportError:
    from . import views

app_name = 'admissions'

urlpatterns = [
    path('entranceexam/', getattr(views, 'EntranceExamListView').as_view(), name='entranceexam_list'),
    path('entranceexam/create/', getattr(views, 'EntranceExamCreateView').as_view(), name='entranceexam_create'),
    path('entranceexam/<int:pk>/', getattr(views, 'EntranceExamDetailView').as_view(), name='entranceexam_detail'),
    path('entranceexam/<int:pk>/edit/', getattr(views, 'EntranceExamUpdateView').as_view(), name='entranceexam_edit'),
    path('entranceexam/<int:pk>/delete/', getattr(views, 'EntranceExamDeleteView').as_view(), name='entranceexam_delete'),
    path('entranceexam/<int:master_pk>/add-item/', getattr(views, 'EntranceExamItemCreateView').as_view(), name='entranceexam_add_item'),
    path('entranceexam/<int:master_pk>/allocate/', getattr(views, 'EntranceExamAllocationCreateView').as_view(), name='entranceexam_allocate'),
    path('entranceexam/bulk-update/', getattr(views, 'EntranceExamBulkStatusUpdateView').as_view(), name='entranceexam_bulk_update'),
    path('entranceexam/export/csv/', getattr(views, 'EntranceExamExportCSVView').as_view(), name='entranceexam_export_csv'),
    path('entranceexam/export/json/', getattr(views, 'EntranceExamExportJSONView').as_view(), name='entranceexam_export_json'),
    path('entranceexam/api/list/', getattr(views, 'EntranceExamAPIListView').as_view(), name='entranceexam_api_list'),
    path('entranceexam/<int:pk>/api/metrics/', getattr(views, 'EntranceExamAPIMetricsView').as_view(), name='entranceexam_api_metrics'),
    path('entranceexam/dashboard/', getattr(views, 'EntranceExamDashboardView', getattr(views, 'EntranceExamListView')).as_view(), name='entranceexam_dashboard'),
    path('entranceexam/analytics/', getattr(views, 'EntranceExamAnalyticsView', getattr(views, 'EntranceExamListView')).as_view(), name='entranceexam_analytics'),
]

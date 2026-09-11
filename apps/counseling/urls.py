"""URL Routing for EduFlow Counseling Cases & Student Support Plans (CounselingCases)."""
from django.urls import path
try:
    from . import views_counselingcases as views
except ImportError:
    from . import views

app_name = 'counseling'

urlpatterns = [
    path('counselingcases/', getattr(views, 'CounselingCasesListView').as_view(), name='counselingcases_list'),
    path('counselingcases/create/', getattr(views, 'CounselingCasesCreateView').as_view(), name='counselingcases_create'),
    path('counselingcases/<int:pk>/', getattr(views, 'CounselingCasesDetailView').as_view(), name='counselingcases_detail'),
    path('counselingcases/<int:pk>/edit/', getattr(views, 'CounselingCasesUpdateView').as_view(), name='counselingcases_edit'),
    path('counselingcases/<int:pk>/delete/', getattr(views, 'CounselingCasesDeleteView').as_view(), name='counselingcases_delete'),
    path('counselingcases/<int:master_pk>/add-item/', getattr(views, 'CounselingCasesItemCreateView').as_view(), name='counselingcases_add_item'),
    path('counselingcases/<int:master_pk>/allocate/', getattr(views, 'CounselingCasesAllocationCreateView').as_view(), name='counselingcases_allocate'),
    path('counselingcases/bulk-update/', getattr(views, 'CounselingCasesBulkStatusUpdateView').as_view(), name='counselingcases_bulk_update'),
    path('counselingcases/export/csv/', getattr(views, 'CounselingCasesExportCSVView').as_view(), name='counselingcases_export_csv'),
    path('counselingcases/export/json/', getattr(views, 'CounselingCasesExportJSONView').as_view(), name='counselingcases_export_json'),
    path('counselingcases/api/list/', getattr(views, 'CounselingCasesAPIListView').as_view(), name='counselingcases_api_list'),
    path('counselingcases/<int:pk>/api/metrics/', getattr(views, 'CounselingCasesAPIMetricsView').as_view(), name='counselingcases_api_metrics'),
    path('counselingcases/dashboard/', getattr(views, 'CounselingCasesDashboardView', getattr(views, 'CounselingCasesListView')).as_view(), name='counselingcases_dashboard'),
    path('counselingcases/analytics/', getattr(views, 'CounselingCasesAnalyticsView', getattr(views, 'CounselingCasesListView')).as_view(), name='counselingcases_analytics'),
]

"""URL Routing for EduFlow Staff Performance Appraisals & Reviews (Appraisal)."""
from django.urls import path
try:
    from . import views_appraisal as views
except ImportError:
    from . import views

app_name = 'staff'

urlpatterns = [
    path('appraisal/', getattr(views, 'AppraisalListView').as_view(), name='appraisal_list'),
    path('appraisal/create/', getattr(views, 'AppraisalCreateView').as_view(), name='appraisal_create'),
    path('appraisal/<int:pk>/', getattr(views, 'AppraisalDetailView').as_view(), name='appraisal_detail'),
    path('appraisal/<int:pk>/edit/', getattr(views, 'AppraisalUpdateView').as_view(), name='appraisal_edit'),
    path('appraisal/<int:pk>/delete/', getattr(views, 'AppraisalDeleteView').as_view(), name='appraisal_delete'),
    path('appraisal/<int:master_pk>/add-item/', getattr(views, 'AppraisalItemCreateView').as_view(), name='appraisal_add_item'),
    path('appraisal/<int:master_pk>/allocate/', getattr(views, 'AppraisalAllocationCreateView').as_view(), name='appraisal_allocate'),
    path('appraisal/bulk-update/', getattr(views, 'AppraisalBulkStatusUpdateView').as_view(), name='appraisal_bulk_update'),
    path('appraisal/export/csv/', getattr(views, 'AppraisalExportCSVView').as_view(), name='appraisal_export_csv'),
    path('appraisal/export/json/', getattr(views, 'AppraisalExportJSONView').as_view(), name='appraisal_export_json'),
    path('appraisal/api/list/', getattr(views, 'AppraisalAPIListView').as_view(), name='appraisal_api_list'),
    path('appraisal/<int:pk>/api/metrics/', getattr(views, 'AppraisalAPIMetricsView').as_view(), name='appraisal_api_metrics'),
    path('appraisal/dashboard/', getattr(views, 'AppraisalDashboardView', getattr(views, 'AppraisalListView')).as_view(), name='appraisal_dashboard'),
    path('appraisal/analytics/', getattr(views, 'AppraisalAnalyticsView', getattr(views, 'AppraisalListView')).as_view(), name='appraisal_analytics'),
]

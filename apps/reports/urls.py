"""URL Routing for EduFlow Global Search, Audit Logs, Master Reports & CLI (MasterReports)."""
from django.urls import path
try:
    from . import views_masterreports as views
except ImportError:
    from . import views

app_name = 'reports'

urlpatterns = [
    path('masterreports/', getattr(views, 'MasterReportsListView').as_view(), name='masterreports_list'),
    path('masterreports/create/', getattr(views, 'MasterReportsCreateView').as_view(), name='masterreports_create'),
    path('masterreports/<int:pk>/', getattr(views, 'MasterReportsDetailView').as_view(), name='masterreports_detail'),
    path('masterreports/<int:pk>/edit/', getattr(views, 'MasterReportsUpdateView').as_view(), name='masterreports_edit'),
    path('masterreports/<int:pk>/delete/', getattr(views, 'MasterReportsDeleteView').as_view(), name='masterreports_delete'),
    path('masterreports/<int:master_pk>/add-item/', getattr(views, 'MasterReportsItemCreateView').as_view(), name='masterreports_add_item'),
    path('masterreports/<int:master_pk>/allocate/', getattr(views, 'MasterReportsAllocationCreateView').as_view(), name='masterreports_allocate'),
    path('masterreports/bulk-update/', getattr(views, 'MasterReportsBulkStatusUpdateView').as_view(), name='masterreports_bulk_update'),
    path('masterreports/export/csv/', getattr(views, 'MasterReportsExportCSVView').as_view(), name='masterreports_export_csv'),
    path('masterreports/export/json/', getattr(views, 'MasterReportsExportJSONView').as_view(), name='masterreports_export_json'),
    path('masterreports/api/list/', getattr(views, 'MasterReportsAPIListView').as_view(), name='masterreports_api_list'),
    path('masterreports/<int:pk>/api/metrics/', getattr(views, 'MasterReportsAPIMetricsView').as_view(), name='masterreports_api_metrics'),
    path('masterreports/dashboard/', getattr(views, 'MasterReportsDashboardView', getattr(views, 'MasterReportsListView')).as_view(), name='masterreports_dashboard'),
    path('masterreports/analytics/', getattr(views, 'MasterReportsAnalyticsView', getattr(views, 'MasterReportsListView')).as_view(), name='masterreports_analytics'),
]

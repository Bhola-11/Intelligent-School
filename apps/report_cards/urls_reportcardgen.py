"""URL Routing for EduFlow Report Cards Generation & Teacher Remarks (ReportCardGen)."""
from django.urls import path
try:
    from . import views_reportcardgen as views
except ImportError:
    from . import views

app_name = 'report_cards'

urlpatterns = [
    path('reportcardgen/', getattr(views, 'ReportCardGenListView').as_view(), name='reportcardgen_list'),
    path('reportcardgen/create/', getattr(views, 'ReportCardGenCreateView').as_view(), name='reportcardgen_create'),
    path('reportcardgen/<int:pk>/', getattr(views, 'ReportCardGenDetailView').as_view(), name='reportcardgen_detail'),
    path('reportcardgen/<int:pk>/edit/', getattr(views, 'ReportCardGenUpdateView').as_view(), name='reportcardgen_edit'),
    path('reportcardgen/<int:pk>/delete/', getattr(views, 'ReportCardGenDeleteView').as_view(), name='reportcardgen_delete'),
    path('reportcardgen/<int:master_pk>/add-item/', getattr(views, 'ReportCardGenItemCreateView').as_view(), name='reportcardgen_add_item'),
    path('reportcardgen/<int:master_pk>/allocate/', getattr(views, 'ReportCardGenAllocationCreateView').as_view(), name='reportcardgen_allocate'),
    path('reportcardgen/bulk-update/', getattr(views, 'ReportCardGenBulkStatusUpdateView').as_view(), name='reportcardgen_bulk_update'),
    path('reportcardgen/export/csv/', getattr(views, 'ReportCardGenExportCSVView').as_view(), name='reportcardgen_export_csv'),
    path('reportcardgen/export/json/', getattr(views, 'ReportCardGenExportJSONView').as_view(), name='reportcardgen_export_json'),
    path('reportcardgen/api/list/', getattr(views, 'ReportCardGenAPIListView').as_view(), name='reportcardgen_api_list'),
    path('reportcardgen/<int:pk>/api/metrics/', getattr(views, 'ReportCardGenAPIMetricsView').as_view(), name='reportcardgen_api_metrics'),
    path('reportcardgen/dashboard/', getattr(views, 'ReportCardGenDashboardView', getattr(views, 'ReportCardGenListView')).as_view(), name='reportcardgen_dashboard'),
    path('reportcardgen/analytics/', getattr(views, 'ReportCardGenAnalyticsView', getattr(views, 'ReportCardGenListView')).as_view(), name='reportcardgen_analytics'),
]

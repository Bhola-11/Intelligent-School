"""URL Routing for EduFlow Financial Statements & Cash Registers (FinancialReports)."""
from django.urls import path
try:
    from . import views_financialreports as views
except ImportError:
    from . import views

app_name = 'accounting'

urlpatterns = [
    path('financialreports/', getattr(views, 'FinancialReportsListView').as_view(), name='financialreports_list'),
    path('financialreports/create/', getattr(views, 'FinancialReportsCreateView').as_view(), name='financialreports_create'),
    path('financialreports/<int:pk>/', getattr(views, 'FinancialReportsDetailView').as_view(), name='financialreports_detail'),
    path('financialreports/<int:pk>/edit/', getattr(views, 'FinancialReportsUpdateView').as_view(), name='financialreports_edit'),
    path('financialreports/<int:pk>/delete/', getattr(views, 'FinancialReportsDeleteView').as_view(), name='financialreports_delete'),
    path('financialreports/<int:master_pk>/add-item/', getattr(views, 'FinancialReportsItemCreateView').as_view(), name='financialreports_add_item'),
    path('financialreports/<int:master_pk>/allocate/', getattr(views, 'FinancialReportsAllocationCreateView').as_view(), name='financialreports_allocate'),
    path('financialreports/bulk-update/', getattr(views, 'FinancialReportsBulkStatusUpdateView').as_view(), name='financialreports_bulk_update'),
    path('financialreports/export/csv/', getattr(views, 'FinancialReportsExportCSVView').as_view(), name='financialreports_export_csv'),
    path('financialreports/export/json/', getattr(views, 'FinancialReportsExportJSONView').as_view(), name='financialreports_export_json'),
    path('financialreports/api/list/', getattr(views, 'FinancialReportsAPIListView').as_view(), name='financialreports_api_list'),
    path('financialreports/<int:pk>/api/metrics/', getattr(views, 'FinancialReportsAPIMetricsView').as_view(), name='financialreports_api_metrics'),
    path('financialreports/dashboard/', getattr(views, 'FinancialReportsDashboardView', getattr(views, 'FinancialReportsListView')).as_view(), name='financialreports_dashboard'),
    path('financialreports/analytics/', getattr(views, 'FinancialReportsAnalyticsView', getattr(views, 'FinancialReportsListView')).as_view(), name='financialreports_analytics'),
]

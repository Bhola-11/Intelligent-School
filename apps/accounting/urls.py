"""URL Routing for EduFlow Chart of Accounts & Financial Ledger (ChartOfAccounts)."""
from django.urls import path
try:
    from . import views_chartofaccounts as views
except ImportError:
    from . import views

app_name = 'accounting'

urlpatterns = [
    path('chartofaccounts/', getattr(views, 'ChartOfAccountsListView').as_view(), name='chartofaccounts_list'),
    path('chartofaccounts/create/', getattr(views, 'ChartOfAccountsCreateView').as_view(), name='chartofaccounts_create'),
    path('chartofaccounts/<int:pk>/', getattr(views, 'ChartOfAccountsDetailView').as_view(), name='chartofaccounts_detail'),
    path('chartofaccounts/<int:pk>/edit/', getattr(views, 'ChartOfAccountsUpdateView').as_view(), name='chartofaccounts_edit'),
    path('chartofaccounts/<int:pk>/delete/', getattr(views, 'ChartOfAccountsDeleteView').as_view(), name='chartofaccounts_delete'),
    path('chartofaccounts/<int:master_pk>/add-item/', getattr(views, 'ChartOfAccountsItemCreateView').as_view(), name='chartofaccounts_add_item'),
    path('chartofaccounts/<int:master_pk>/allocate/', getattr(views, 'ChartOfAccountsAllocationCreateView').as_view(), name='chartofaccounts_allocate'),
    path('chartofaccounts/bulk-update/', getattr(views, 'ChartOfAccountsBulkStatusUpdateView').as_view(), name='chartofaccounts_bulk_update'),
    path('chartofaccounts/export/csv/', getattr(views, 'ChartOfAccountsExportCSVView').as_view(), name='chartofaccounts_export_csv'),
    path('chartofaccounts/export/json/', getattr(views, 'ChartOfAccountsExportJSONView').as_view(), name='chartofaccounts_export_json'),
    path('chartofaccounts/api/list/', getattr(views, 'ChartOfAccountsAPIListView').as_view(), name='chartofaccounts_api_list'),
    path('chartofaccounts/<int:pk>/api/metrics/', getattr(views, 'ChartOfAccountsAPIMetricsView').as_view(), name='chartofaccounts_api_metrics'),
    path('chartofaccounts/dashboard/', getattr(views, 'ChartOfAccountsDashboardView', getattr(views, 'ChartOfAccountsListView')).as_view(), name='chartofaccounts_dashboard'),
    path('chartofaccounts/analytics/', getattr(views, 'ChartOfAccountsAnalyticsView', getattr(views, 'ChartOfAccountsListView')).as_view(), name='chartofaccounts_analytics'),
]

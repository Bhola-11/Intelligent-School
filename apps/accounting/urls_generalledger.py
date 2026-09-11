"""URL Routing for EduFlow General Ledger & Double-Entry Journals (GeneralLedger)."""
from django.urls import path
try:
    from . import views_generalledger as views
except ImportError:
    from . import views

app_name = 'accounting'

urlpatterns = [
    path('generalledger/', getattr(views, 'GeneralLedgerListView').as_view(), name='generalledger_list'),
    path('generalledger/create/', getattr(views, 'GeneralLedgerCreateView').as_view(), name='generalledger_create'),
    path('generalledger/<int:pk>/', getattr(views, 'GeneralLedgerDetailView').as_view(), name='generalledger_detail'),
    path('generalledger/<int:pk>/edit/', getattr(views, 'GeneralLedgerUpdateView').as_view(), name='generalledger_edit'),
    path('generalledger/<int:pk>/delete/', getattr(views, 'GeneralLedgerDeleteView').as_view(), name='generalledger_delete'),
    path('generalledger/<int:master_pk>/add-item/', getattr(views, 'GeneralLedgerItemCreateView').as_view(), name='generalledger_add_item'),
    path('generalledger/<int:master_pk>/allocate/', getattr(views, 'GeneralLedgerAllocationCreateView').as_view(), name='generalledger_allocate'),
    path('generalledger/bulk-update/', getattr(views, 'GeneralLedgerBulkStatusUpdateView').as_view(), name='generalledger_bulk_update'),
    path('generalledger/export/csv/', getattr(views, 'GeneralLedgerExportCSVView').as_view(), name='generalledger_export_csv'),
    path('generalledger/export/json/', getattr(views, 'GeneralLedgerExportJSONView').as_view(), name='generalledger_export_json'),
    path('generalledger/api/list/', getattr(views, 'GeneralLedgerAPIListView').as_view(), name='generalledger_api_list'),
    path('generalledger/<int:pk>/api/metrics/', getattr(views, 'GeneralLedgerAPIMetricsView').as_view(), name='generalledger_api_metrics'),
    path('generalledger/dashboard/', getattr(views, 'GeneralLedgerDashboardView', getattr(views, 'GeneralLedgerListView')).as_view(), name='generalledger_dashboard'),
    path('generalledger/analytics/', getattr(views, 'GeneralLedgerAnalyticsView', getattr(views, 'GeneralLedgerListView')).as_view(), name='generalledger_analytics'),
]

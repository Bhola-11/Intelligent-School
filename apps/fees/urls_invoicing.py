"""URL Routing for EduFlow Student Fee Invoicing & Billing Engine (Invoicing)."""
from django.urls import path
try:
    from . import views_invoicing as views
except ImportError:
    from . import views

app_name = 'fees'

urlpatterns = [
    path('invoicing/', getattr(views, 'InvoicingListView').as_view(), name='invoicing_list'),
    path('invoicing/create/', getattr(views, 'InvoicingCreateView').as_view(), name='invoicing_create'),
    path('invoicing/<int:pk>/', getattr(views, 'InvoicingDetailView').as_view(), name='invoicing_detail'),
    path('invoicing/<int:pk>/edit/', getattr(views, 'InvoicingUpdateView').as_view(), name='invoicing_edit'),
    path('invoicing/<int:pk>/delete/', getattr(views, 'InvoicingDeleteView').as_view(), name='invoicing_delete'),
    path('invoicing/<int:master_pk>/add-item/', getattr(views, 'InvoicingItemCreateView').as_view(), name='invoicing_add_item'),
    path('invoicing/<int:master_pk>/allocate/', getattr(views, 'InvoicingAllocationCreateView').as_view(), name='invoicing_allocate'),
    path('invoicing/bulk-update/', getattr(views, 'InvoicingBulkStatusUpdateView').as_view(), name='invoicing_bulk_update'),
    path('invoicing/export/csv/', getattr(views, 'InvoicingExportCSVView').as_view(), name='invoicing_export_csv'),
    path('invoicing/export/json/', getattr(views, 'InvoicingExportJSONView').as_view(), name='invoicing_export_json'),
    path('invoicing/api/list/', getattr(views, 'InvoicingAPIListView').as_view(), name='invoicing_api_list'),
    path('invoicing/<int:pk>/api/metrics/', getattr(views, 'InvoicingAPIMetricsView').as_view(), name='invoicing_api_metrics'),
    path('invoicing/dashboard/', getattr(views, 'InvoicingDashboardView', getattr(views, 'InvoicingListView')).as_view(), name='invoicing_dashboard'),
    path('invoicing/analytics/', getattr(views, 'InvoicingAnalyticsView', getattr(views, 'InvoicingListView')).as_view(), name='invoicing_analytics'),
]

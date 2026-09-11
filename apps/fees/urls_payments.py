"""URL Routing for EduFlow Fee Payments, Receipts & Gateways (Payments)."""
from django.urls import path
try:
    from . import views_payments as views
except ImportError:
    from . import views

app_name = 'fees'

urlpatterns = [
    path('payments/', getattr(views, 'PaymentsListView').as_view(), name='payments_list'),
    path('payments/create/', getattr(views, 'PaymentsCreateView').as_view(), name='payments_create'),
    path('payments/<int:pk>/', getattr(views, 'PaymentsDetailView').as_view(), name='payments_detail'),
    path('payments/<int:pk>/edit/', getattr(views, 'PaymentsUpdateView').as_view(), name='payments_edit'),
    path('payments/<int:pk>/delete/', getattr(views, 'PaymentsDeleteView').as_view(), name='payments_delete'),
    path('payments/<int:master_pk>/add-item/', getattr(views, 'PaymentsItemCreateView').as_view(), name='payments_add_item'),
    path('payments/<int:master_pk>/allocate/', getattr(views, 'PaymentsAllocationCreateView').as_view(), name='payments_allocate'),
    path('payments/bulk-update/', getattr(views, 'PaymentsBulkStatusUpdateView').as_view(), name='payments_bulk_update'),
    path('payments/export/csv/', getattr(views, 'PaymentsExportCSVView').as_view(), name='payments_export_csv'),
    path('payments/export/json/', getattr(views, 'PaymentsExportJSONView').as_view(), name='payments_export_json'),
    path('payments/api/list/', getattr(views, 'PaymentsAPIListView').as_view(), name='payments_api_list'),
    path('payments/<int:pk>/api/metrics/', getattr(views, 'PaymentsAPIMetricsView').as_view(), name='payments_api_metrics'),
    path('payments/dashboard/', getattr(views, 'PaymentsDashboardView', getattr(views, 'PaymentsListView')).as_view(), name='payments_dashboard'),
    path('payments/analytics/', getattr(views, 'PaymentsAnalyticsView', getattr(views, 'PaymentsListView')).as_view(), name='payments_analytics'),
]

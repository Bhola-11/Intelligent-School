"""URL Routing for EduFlow Expense Vouchers & Payment Approvals (Vouchers)."""
from django.urls import path
try:
    from . import views_vouchers as views
except ImportError:
    from . import views

app_name = 'accounting'

urlpatterns = [
    path('vouchers/', getattr(views, 'VouchersListView').as_view(), name='vouchers_list'),
    path('vouchers/create/', getattr(views, 'VouchersCreateView').as_view(), name='vouchers_create'),
    path('vouchers/<int:pk>/', getattr(views, 'VouchersDetailView').as_view(), name='vouchers_detail'),
    path('vouchers/<int:pk>/edit/', getattr(views, 'VouchersUpdateView').as_view(), name='vouchers_edit'),
    path('vouchers/<int:pk>/delete/', getattr(views, 'VouchersDeleteView').as_view(), name='vouchers_delete'),
    path('vouchers/<int:master_pk>/add-item/', getattr(views, 'VouchersItemCreateView').as_view(), name='vouchers_add_item'),
    path('vouchers/<int:master_pk>/allocate/', getattr(views, 'VouchersAllocationCreateView').as_view(), name='vouchers_allocate'),
    path('vouchers/bulk-update/', getattr(views, 'VouchersBulkStatusUpdateView').as_view(), name='vouchers_bulk_update'),
    path('vouchers/export/csv/', getattr(views, 'VouchersExportCSVView').as_view(), name='vouchers_export_csv'),
    path('vouchers/export/json/', getattr(views, 'VouchersExportJSONView').as_view(), name='vouchers_export_json'),
    path('vouchers/api/list/', getattr(views, 'VouchersAPIListView').as_view(), name='vouchers_api_list'),
    path('vouchers/<int:pk>/api/metrics/', getattr(views, 'VouchersAPIMetricsView').as_view(), name='vouchers_api_metrics'),
    path('vouchers/dashboard/', getattr(views, 'VouchersDashboardView', getattr(views, 'VouchersListView')).as_view(), name='vouchers_dashboard'),
    path('vouchers/analytics/', getattr(views, 'VouchersAnalyticsView', getattr(views, 'VouchersListView')).as_view(), name='vouchers_analytics'),
]

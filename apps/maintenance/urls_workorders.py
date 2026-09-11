"""URL Routing for EduFlow Technician Allocations & Maintenance Costs (WorkOrders)."""
from django.urls import path
try:
    from . import views_workorders as views
except ImportError:
    from . import views

app_name = 'maintenance'

urlpatterns = [
    path('workorders/', getattr(views, 'WorkOrdersListView').as_view(), name='workorders_list'),
    path('workorders/create/', getattr(views, 'WorkOrdersCreateView').as_view(), name='workorders_create'),
    path('workorders/<int:pk>/', getattr(views, 'WorkOrdersDetailView').as_view(), name='workorders_detail'),
    path('workorders/<int:pk>/edit/', getattr(views, 'WorkOrdersUpdateView').as_view(), name='workorders_edit'),
    path('workorders/<int:pk>/delete/', getattr(views, 'WorkOrdersDeleteView').as_view(), name='workorders_delete'),
    path('workorders/<int:master_pk>/add-item/', getattr(views, 'WorkOrdersItemCreateView').as_view(), name='workorders_add_item'),
    path('workorders/<int:master_pk>/allocate/', getattr(views, 'WorkOrdersAllocationCreateView').as_view(), name='workorders_allocate'),
    path('workorders/bulk-update/', getattr(views, 'WorkOrdersBulkStatusUpdateView').as_view(), name='workorders_bulk_update'),
    path('workorders/export/csv/', getattr(views, 'WorkOrdersExportCSVView').as_view(), name='workorders_export_csv'),
    path('workorders/export/json/', getattr(views, 'WorkOrdersExportJSONView').as_view(), name='workorders_export_json'),
    path('workorders/api/list/', getattr(views, 'WorkOrdersAPIListView').as_view(), name='workorders_api_list'),
    path('workorders/<int:pk>/api/metrics/', getattr(views, 'WorkOrdersAPIMetricsView').as_view(), name='workorders_api_metrics'),
    path('workorders/dashboard/', getattr(views, 'WorkOrdersDashboardView', getattr(views, 'WorkOrdersListView')).as_view(), name='workorders_dashboard'),
    path('workorders/analytics/', getattr(views, 'WorkOrdersAnalyticsView', getattr(views, 'WorkOrdersListView')).as_view(), name='workorders_analytics'),
]

"""URL Routing for EduFlow Staff Leave Applications & Approval Workflows (StaffLeaves)."""
from django.urls import path
try:
    from . import views_staffleaves as views
except ImportError:
    from . import views

app_name = 'leaves'

urlpatterns = [
    path('staffleaves/', getattr(views, 'StaffLeavesListView').as_view(), name='staffleaves_list'),
    path('staffleaves/create/', getattr(views, 'StaffLeavesCreateView').as_view(), name='staffleaves_create'),
    path('staffleaves/<int:pk>/', getattr(views, 'StaffLeavesDetailView').as_view(), name='staffleaves_detail'),
    path('staffleaves/<int:pk>/edit/', getattr(views, 'StaffLeavesUpdateView').as_view(), name='staffleaves_edit'),
    path('staffleaves/<int:pk>/delete/', getattr(views, 'StaffLeavesDeleteView').as_view(), name='staffleaves_delete'),
    path('staffleaves/<int:master_pk>/add-item/', getattr(views, 'StaffLeavesItemCreateView').as_view(), name='staffleaves_add_item'),
    path('staffleaves/<int:master_pk>/allocate/', getattr(views, 'StaffLeavesAllocationCreateView').as_view(), name='staffleaves_allocate'),
    path('staffleaves/bulk-update/', getattr(views, 'StaffLeavesBulkStatusUpdateView').as_view(), name='staffleaves_bulk_update'),
    path('staffleaves/export/csv/', getattr(views, 'StaffLeavesExportCSVView').as_view(), name='staffleaves_export_csv'),
    path('staffleaves/export/json/', getattr(views, 'StaffLeavesExportJSONView').as_view(), name='staffleaves_export_json'),
    path('staffleaves/api/list/', getattr(views, 'StaffLeavesAPIListView').as_view(), name='staffleaves_api_list'),
    path('staffleaves/<int:pk>/api/metrics/', getattr(views, 'StaffLeavesAPIMetricsView').as_view(), name='staffleaves_api_metrics'),
    path('staffleaves/dashboard/', getattr(views, 'StaffLeavesDashboardView', getattr(views, 'StaffLeavesListView')).as_view(), name='staffleaves_dashboard'),
    path('staffleaves/analytics/', getattr(views, 'StaffLeavesAnalyticsView', getattr(views, 'StaffLeavesListView')).as_view(), name='staffleaves_analytics'),
]

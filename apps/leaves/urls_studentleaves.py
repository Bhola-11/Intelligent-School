"""URL Routing for EduFlow Student Leave Requests & Parent Consents (StudentLeaves)."""
from django.urls import path
try:
    from . import views_studentleaves as views
except ImportError:
    from . import views

app_name = 'leaves'

urlpatterns = [
    path('studentleaves/', getattr(views, 'StudentLeavesListView').as_view(), name='studentleaves_list'),
    path('studentleaves/create/', getattr(views, 'StudentLeavesCreateView').as_view(), name='studentleaves_create'),
    path('studentleaves/<int:pk>/', getattr(views, 'StudentLeavesDetailView').as_view(), name='studentleaves_detail'),
    path('studentleaves/<int:pk>/edit/', getattr(views, 'StudentLeavesUpdateView').as_view(), name='studentleaves_edit'),
    path('studentleaves/<int:pk>/delete/', getattr(views, 'StudentLeavesDeleteView').as_view(), name='studentleaves_delete'),
    path('studentleaves/<int:master_pk>/add-item/', getattr(views, 'StudentLeavesItemCreateView').as_view(), name='studentleaves_add_item'),
    path('studentleaves/<int:master_pk>/allocate/', getattr(views, 'StudentLeavesAllocationCreateView').as_view(), name='studentleaves_allocate'),
    path('studentleaves/bulk-update/', getattr(views, 'StudentLeavesBulkStatusUpdateView').as_view(), name='studentleaves_bulk_update'),
    path('studentleaves/export/csv/', getattr(views, 'StudentLeavesExportCSVView').as_view(), name='studentleaves_export_csv'),
    path('studentleaves/export/json/', getattr(views, 'StudentLeavesExportJSONView').as_view(), name='studentleaves_export_json'),
    path('studentleaves/api/list/', getattr(views, 'StudentLeavesAPIListView').as_view(), name='studentleaves_api_list'),
    path('studentleaves/<int:pk>/api/metrics/', getattr(views, 'StudentLeavesAPIMetricsView').as_view(), name='studentleaves_api_metrics'),
    path('studentleaves/dashboard/', getattr(views, 'StudentLeavesDashboardView', getattr(views, 'StudentLeavesListView')).as_view(), name='studentleaves_dashboard'),
    path('studentleaves/analytics/', getattr(views, 'StudentLeavesAnalyticsView', getattr(views, 'StudentLeavesListView')).as_view(), name='studentleaves_analytics'),
]

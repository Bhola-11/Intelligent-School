"""URL Routing for EduFlow Staff Profiles & Employee Directory (StaffDirectory)."""
from django.urls import path
try:
    from . import views_staffdirectory as views
except ImportError:
    from . import views

app_name = 'staff'

urlpatterns = [
    path('staffdirectory/', getattr(views, 'StaffDirectoryListView').as_view(), name='staffdirectory_list'),
    path('staffdirectory/create/', getattr(views, 'StaffDirectoryCreateView').as_view(), name='staffdirectory_create'),
    path('staffdirectory/<int:pk>/', getattr(views, 'StaffDirectoryDetailView').as_view(), name='staffdirectory_detail'),
    path('staffdirectory/<int:pk>/edit/', getattr(views, 'StaffDirectoryUpdateView').as_view(), name='staffdirectory_edit'),
    path('staffdirectory/<int:pk>/delete/', getattr(views, 'StaffDirectoryDeleteView').as_view(), name='staffdirectory_delete'),
    path('staffdirectory/<int:master_pk>/add-item/', getattr(views, 'StaffDirectoryItemCreateView').as_view(), name='staffdirectory_add_item'),
    path('staffdirectory/<int:master_pk>/allocate/', getattr(views, 'StaffDirectoryAllocationCreateView').as_view(), name='staffdirectory_allocate'),
    path('staffdirectory/bulk-update/', getattr(views, 'StaffDirectoryBulkStatusUpdateView').as_view(), name='staffdirectory_bulk_update'),
    path('staffdirectory/export/csv/', getattr(views, 'StaffDirectoryExportCSVView').as_view(), name='staffdirectory_export_csv'),
    path('staffdirectory/export/json/', getattr(views, 'StaffDirectoryExportJSONView').as_view(), name='staffdirectory_export_json'),
    path('staffdirectory/api/list/', getattr(views, 'StaffDirectoryAPIListView').as_view(), name='staffdirectory_api_list'),
    path('staffdirectory/<int:pk>/api/metrics/', getattr(views, 'StaffDirectoryAPIMetricsView').as_view(), name='staffdirectory_api_metrics'),
    path('staffdirectory/dashboard/', getattr(views, 'StaffDirectoryDashboardView', getattr(views, 'StaffDirectoryListView')).as_view(), name='staffdirectory_dashboard'),
    path('staffdirectory/analytics/', getattr(views, 'StaffDirectoryAnalyticsView', getattr(views, 'StaffDirectoryListView')).as_view(), name='staffdirectory_analytics'),
]

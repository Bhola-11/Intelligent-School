"""URL Routing for EduFlow Department Head (HOD) Overview (HODDesk)."""
from django.urls import path
try:
    from . import views_hoddesk as views
except ImportError:
    from . import views

app_name = 'portals'

urlpatterns = [
    path('hoddesk/', getattr(views, 'HODDeskListView').as_view(), name='hoddesk_list'),
    path('hoddesk/create/', getattr(views, 'HODDeskCreateView').as_view(), name='hoddesk_create'),
    path('hoddesk/<int:pk>/', getattr(views, 'HODDeskDetailView').as_view(), name='hoddesk_detail'),
    path('hoddesk/<int:pk>/edit/', getattr(views, 'HODDeskUpdateView').as_view(), name='hoddesk_edit'),
    path('hoddesk/<int:pk>/delete/', getattr(views, 'HODDeskDeleteView').as_view(), name='hoddesk_delete'),
    path('hoddesk/<int:master_pk>/add-item/', getattr(views, 'HODDeskItemCreateView').as_view(), name='hoddesk_add_item'),
    path('hoddesk/<int:master_pk>/allocate/', getattr(views, 'HODDeskAllocationCreateView').as_view(), name='hoddesk_allocate'),
    path('hoddesk/bulk-update/', getattr(views, 'HODDeskBulkStatusUpdateView').as_view(), name='hoddesk_bulk_update'),
    path('hoddesk/export/csv/', getattr(views, 'HODDeskExportCSVView').as_view(), name='hoddesk_export_csv'),
    path('hoddesk/export/json/', getattr(views, 'HODDeskExportJSONView').as_view(), name='hoddesk_export_json'),
    path('hoddesk/api/list/', getattr(views, 'HODDeskAPIListView').as_view(), name='hoddesk_api_list'),
    path('hoddesk/<int:pk>/api/metrics/', getattr(views, 'HODDeskAPIMetricsView').as_view(), name='hoddesk_api_metrics'),
    path('hoddesk/dashboard/', getattr(views, 'HODDeskDashboardView', getattr(views, 'HODDeskListView')).as_view(), name='hoddesk_dashboard'),
    path('hoddesk/analytics/', getattr(views, 'HODDeskAnalyticsView', getattr(views, 'HODDeskListView')).as_view(), name='hoddesk_analytics'),
]

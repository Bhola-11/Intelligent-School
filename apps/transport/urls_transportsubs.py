"""URL Routing for EduFlow Student Transport Subscriptions & Fees (TransportSubs)."""
from django.urls import path
try:
    from . import views_transportsubs as views
except ImportError:
    from . import views

app_name = 'transport'

urlpatterns = [
    path('transportsubs/', getattr(views, 'TransportSubsListView').as_view(), name='transportsubs_list'),
    path('transportsubs/create/', getattr(views, 'TransportSubsCreateView').as_view(), name='transportsubs_create'),
    path('transportsubs/<int:pk>/', getattr(views, 'TransportSubsDetailView').as_view(), name='transportsubs_detail'),
    path('transportsubs/<int:pk>/edit/', getattr(views, 'TransportSubsUpdateView').as_view(), name='transportsubs_edit'),
    path('transportsubs/<int:pk>/delete/', getattr(views, 'TransportSubsDeleteView').as_view(), name='transportsubs_delete'),
    path('transportsubs/<int:master_pk>/add-item/', getattr(views, 'TransportSubsItemCreateView').as_view(), name='transportsubs_add_item'),
    path('transportsubs/<int:master_pk>/allocate/', getattr(views, 'TransportSubsAllocationCreateView').as_view(), name='transportsubs_allocate'),
    path('transportsubs/bulk-update/', getattr(views, 'TransportSubsBulkStatusUpdateView').as_view(), name='transportsubs_bulk_update'),
    path('transportsubs/export/csv/', getattr(views, 'TransportSubsExportCSVView').as_view(), name='transportsubs_export_csv'),
    path('transportsubs/export/json/', getattr(views, 'TransportSubsExportJSONView').as_view(), name='transportsubs_export_json'),
    path('transportsubs/api/list/', getattr(views, 'TransportSubsAPIListView').as_view(), name='transportsubs_api_list'),
    path('transportsubs/<int:pk>/api/metrics/', getattr(views, 'TransportSubsAPIMetricsView').as_view(), name='transportsubs_api_metrics'),
    path('transportsubs/dashboard/', getattr(views, 'TransportSubsDashboardView', getattr(views, 'TransportSubsListView')).as_view(), name='transportsubs_dashboard'),
    path('transportsubs/analytics/', getattr(views, 'TransportSubsAnalyticsView', getattr(views, 'TransportSubsListView')).as_view(), name='transportsubs_analytics'),
]

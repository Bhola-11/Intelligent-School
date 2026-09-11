"""URL Routing for EduFlow Reception & Front Office Desk (ReceptionDesk)."""
from django.urls import path
try:
    from . import views_receptiondesk as views
except ImportError:
    from . import views

app_name = 'portals'

urlpatterns = [
    path('receptiondesk/', getattr(views, 'ReceptionDeskListView').as_view(), name='receptiondesk_list'),
    path('receptiondesk/create/', getattr(views, 'ReceptionDeskCreateView').as_view(), name='receptiondesk_create'),
    path('receptiondesk/<int:pk>/', getattr(views, 'ReceptionDeskDetailView').as_view(), name='receptiondesk_detail'),
    path('receptiondesk/<int:pk>/edit/', getattr(views, 'ReceptionDeskUpdateView').as_view(), name='receptiondesk_edit'),
    path('receptiondesk/<int:pk>/delete/', getattr(views, 'ReceptionDeskDeleteView').as_view(), name='receptiondesk_delete'),
    path('receptiondesk/<int:master_pk>/add-item/', getattr(views, 'ReceptionDeskItemCreateView').as_view(), name='receptiondesk_add_item'),
    path('receptiondesk/<int:master_pk>/allocate/', getattr(views, 'ReceptionDeskAllocationCreateView').as_view(), name='receptiondesk_allocate'),
    path('receptiondesk/bulk-update/', getattr(views, 'ReceptionDeskBulkStatusUpdateView').as_view(), name='receptiondesk_bulk_update'),
    path('receptiondesk/export/csv/', getattr(views, 'ReceptionDeskExportCSVView').as_view(), name='receptiondesk_export_csv'),
    path('receptiondesk/export/json/', getattr(views, 'ReceptionDeskExportJSONView').as_view(), name='receptiondesk_export_json'),
    path('receptiondesk/api/list/', getattr(views, 'ReceptionDeskAPIListView').as_view(), name='receptiondesk_api_list'),
    path('receptiondesk/<int:pk>/api/metrics/', getattr(views, 'ReceptionDeskAPIMetricsView').as_view(), name='receptiondesk_api_metrics'),
    path('receptiondesk/dashboard/', getattr(views, 'ReceptionDeskDashboardView', getattr(views, 'ReceptionDeskListView')).as_view(), name='receptiondesk_dashboard'),
    path('receptiondesk/analytics/', getattr(views, 'ReceptionDeskAnalyticsView', getattr(views, 'ReceptionDeskListView')).as_view(), name='receptiondesk_analytics'),
]

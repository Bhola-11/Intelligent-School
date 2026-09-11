"""URL Routing for EduFlow Accountant Financial Operations Desk (AccountantDesk)."""
from django.urls import path
try:
    from . import views_accountantdesk as views
except ImportError:
    from . import views

app_name = 'portals'

urlpatterns = [
    path('accountantdesk/', getattr(views, 'AccountantDeskListView').as_view(), name='accountantdesk_list'),
    path('accountantdesk/create/', getattr(views, 'AccountantDeskCreateView').as_view(), name='accountantdesk_create'),
    path('accountantdesk/<int:pk>/', getattr(views, 'AccountantDeskDetailView').as_view(), name='accountantdesk_detail'),
    path('accountantdesk/<int:pk>/edit/', getattr(views, 'AccountantDeskUpdateView').as_view(), name='accountantdesk_edit'),
    path('accountantdesk/<int:pk>/delete/', getattr(views, 'AccountantDeskDeleteView').as_view(), name='accountantdesk_delete'),
    path('accountantdesk/<int:master_pk>/add-item/', getattr(views, 'AccountantDeskItemCreateView').as_view(), name='accountantdesk_add_item'),
    path('accountantdesk/<int:master_pk>/allocate/', getattr(views, 'AccountantDeskAllocationCreateView').as_view(), name='accountantdesk_allocate'),
    path('accountantdesk/bulk-update/', getattr(views, 'AccountantDeskBulkStatusUpdateView').as_view(), name='accountantdesk_bulk_update'),
    path('accountantdesk/export/csv/', getattr(views, 'AccountantDeskExportCSVView').as_view(), name='accountantdesk_export_csv'),
    path('accountantdesk/export/json/', getattr(views, 'AccountantDeskExportJSONView').as_view(), name='accountantdesk_export_json'),
    path('accountantdesk/api/list/', getattr(views, 'AccountantDeskAPIListView').as_view(), name='accountantdesk_api_list'),
    path('accountantdesk/<int:pk>/api/metrics/', getattr(views, 'AccountantDeskAPIMetricsView').as_view(), name='accountantdesk_api_metrics'),
    path('accountantdesk/dashboard/', getattr(views, 'AccountantDeskDashboardView', getattr(views, 'AccountantDeskListView')).as_view(), name='accountantdesk_dashboard'),
    path('accountantdesk/analytics/', getattr(views, 'AccountantDeskAnalyticsView', getattr(views, 'AccountantDeskListView')).as_view(), name='accountantdesk_analytics'),
]

"""URL Routing for EduFlow Notification Engine & Channel Routing (Notifications)."""
from django.urls import path
try:
    from . import views_notifications as views
except ImportError:
    from . import views

app_name = 'notifications'

urlpatterns = [
    path('notifications/', getattr(views, 'NotificationsListView').as_view(), name='notifications_list'),
    path('notifications/create/', getattr(views, 'NotificationsCreateView').as_view(), name='notifications_create'),
    path('notifications/<int:pk>/', getattr(views, 'NotificationsDetailView').as_view(), name='notifications_detail'),
    path('notifications/<int:pk>/edit/', getattr(views, 'NotificationsUpdateView').as_view(), name='notifications_edit'),
    path('notifications/<int:pk>/delete/', getattr(views, 'NotificationsDeleteView').as_view(), name='notifications_delete'),
    path('notifications/<int:master_pk>/add-item/', getattr(views, 'NotificationsItemCreateView').as_view(), name='notifications_add_item'),
    path('notifications/<int:master_pk>/allocate/', getattr(views, 'NotificationsAllocationCreateView').as_view(), name='notifications_allocate'),
    path('notifications/bulk-update/', getattr(views, 'NotificationsBulkStatusUpdateView').as_view(), name='notifications_bulk_update'),
    path('notifications/export/csv/', getattr(views, 'NotificationsExportCSVView').as_view(), name='notifications_export_csv'),
    path('notifications/export/json/', getattr(views, 'NotificationsExportJSONView').as_view(), name='notifications_export_json'),
    path('notifications/api/list/', getattr(views, 'NotificationsAPIListView').as_view(), name='notifications_api_list'),
    path('notifications/<int:pk>/api/metrics/', getattr(views, 'NotificationsAPIMetricsView').as_view(), name='notifications_api_metrics'),
    path('notifications/dashboard/', getattr(views, 'NotificationsDashboardView', getattr(views, 'NotificationsListView')).as_view(), name='notifications_dashboard'),
    path('notifications/analytics/', getattr(views, 'NotificationsAnalyticsView', getattr(views, 'NotificationsListView')).as_view(), name='notifications_analytics'),
]

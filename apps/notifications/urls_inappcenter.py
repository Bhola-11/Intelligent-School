"""URL Routing for EduFlow In-App Notification Center & Alerts (InAppCenter)."""
from django.urls import path
try:
    from . import views_inappcenter as views
except ImportError:
    from . import views

app_name = 'notifications'

urlpatterns = [
    path('inappcenter/', getattr(views, 'InAppCenterListView').as_view(), name='inappcenter_list'),
    path('inappcenter/create/', getattr(views, 'InAppCenterCreateView').as_view(), name='inappcenter_create'),
    path('inappcenter/<int:pk>/', getattr(views, 'InAppCenterDetailView').as_view(), name='inappcenter_detail'),
    path('inappcenter/<int:pk>/edit/', getattr(views, 'InAppCenterUpdateView').as_view(), name='inappcenter_edit'),
    path('inappcenter/<int:pk>/delete/', getattr(views, 'InAppCenterDeleteView').as_view(), name='inappcenter_delete'),
    path('inappcenter/<int:master_pk>/add-item/', getattr(views, 'InAppCenterItemCreateView').as_view(), name='inappcenter_add_item'),
    path('inappcenter/<int:master_pk>/allocate/', getattr(views, 'InAppCenterAllocationCreateView').as_view(), name='inappcenter_allocate'),
    path('inappcenter/bulk-update/', getattr(views, 'InAppCenterBulkStatusUpdateView').as_view(), name='inappcenter_bulk_update'),
    path('inappcenter/export/csv/', getattr(views, 'InAppCenterExportCSVView').as_view(), name='inappcenter_export_csv'),
    path('inappcenter/export/json/', getattr(views, 'InAppCenterExportJSONView').as_view(), name='inappcenter_export_json'),
    path('inappcenter/api/list/', getattr(views, 'InAppCenterAPIListView').as_view(), name='inappcenter_api_list'),
    path('inappcenter/<int:pk>/api/metrics/', getattr(views, 'InAppCenterAPIMetricsView').as_view(), name='inappcenter_api_metrics'),
    path('inappcenter/dashboard/', getattr(views, 'InAppCenterDashboardView', getattr(views, 'InAppCenterListView')).as_view(), name='inappcenter_dashboard'),
    path('inappcenter/analytics/', getattr(views, 'InAppCenterAnalyticsView', getattr(views, 'InAppCenterListView')).as_view(), name='inappcenter_analytics'),
]

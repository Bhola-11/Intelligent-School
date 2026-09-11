"""URL Routing for EduFlow Super Administrator Executive Portal (SuperAdmin)."""
from django.urls import path
try:
    from . import views_superadmin as views
except ImportError:
    from . import views

app_name = 'portals'

urlpatterns = [
    path('superadmin/', getattr(views, 'SuperAdminListView').as_view(), name='superadmin_list'),
    path('superadmin/create/', getattr(views, 'SuperAdminCreateView').as_view(), name='superadmin_create'),
    path('superadmin/<int:pk>/', getattr(views, 'SuperAdminDetailView').as_view(), name='superadmin_detail'),
    path('superadmin/<int:pk>/edit/', getattr(views, 'SuperAdminUpdateView').as_view(), name='superadmin_edit'),
    path('superadmin/<int:pk>/delete/', getattr(views, 'SuperAdminDeleteView').as_view(), name='superadmin_delete'),
    path('superadmin/<int:master_pk>/add-item/', getattr(views, 'SuperAdminItemCreateView').as_view(), name='superadmin_add_item'),
    path('superadmin/<int:master_pk>/allocate/', getattr(views, 'SuperAdminAllocationCreateView').as_view(), name='superadmin_allocate'),
    path('superadmin/bulk-update/', getattr(views, 'SuperAdminBulkStatusUpdateView').as_view(), name='superadmin_bulk_update'),
    path('superadmin/export/csv/', getattr(views, 'SuperAdminExportCSVView').as_view(), name='superadmin_export_csv'),
    path('superadmin/export/json/', getattr(views, 'SuperAdminExportJSONView').as_view(), name='superadmin_export_json'),
    path('superadmin/api/list/', getattr(views, 'SuperAdminAPIListView').as_view(), name='superadmin_api_list'),
    path('superadmin/<int:pk>/api/metrics/', getattr(views, 'SuperAdminAPIMetricsView').as_view(), name='superadmin_api_metrics'),
    path('superadmin/dashboard/', getattr(views, 'SuperAdminDashboardView', getattr(views, 'SuperAdminListView')).as_view(), name='superadmin_dashboard'),
    path('superadmin/analytics/', getattr(views, 'SuperAdminAnalyticsView', getattr(views, 'SuperAdminListView')).as_view(), name='superadmin_analytics'),
]

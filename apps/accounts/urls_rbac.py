"""URL Routing for EduFlow Role-Based Access Control & Permissions (RBAC)."""
from django.urls import path
try:
    from . import views_rbac as views
except ImportError:
    from . import views

app_name = 'accounts'

urlpatterns = [
    path('rbac/', getattr(views, 'RBACListView').as_view(), name='rbac_list'),
    path('rbac/create/', getattr(views, 'RBACCreateView').as_view(), name='rbac_create'),
    path('rbac/<int:pk>/', getattr(views, 'RBACDetailView').as_view(), name='rbac_detail'),
    path('rbac/<int:pk>/edit/', getattr(views, 'RBACUpdateView').as_view(), name='rbac_edit'),
    path('rbac/<int:pk>/delete/', getattr(views, 'RBACDeleteView').as_view(), name='rbac_delete'),
    path('rbac/<int:master_pk>/add-item/', getattr(views, 'RBACItemCreateView').as_view(), name='rbac_add_item'),
    path('rbac/<int:master_pk>/allocate/', getattr(views, 'RBACAllocationCreateView').as_view(), name='rbac_allocate'),
    path('rbac/bulk-update/', getattr(views, 'RBACBulkStatusUpdateView').as_view(), name='rbac_bulk_update'),
    path('rbac/export/csv/', getattr(views, 'RBACExportCSVView').as_view(), name='rbac_export_csv'),
    path('rbac/export/json/', getattr(views, 'RBACExportJSONView').as_view(), name='rbac_export_json'),
    path('rbac/api/list/', getattr(views, 'RBACAPIListView').as_view(), name='rbac_api_list'),
    path('rbac/<int:pk>/api/metrics/', getattr(views, 'RBACAPIMetricsView').as_view(), name='rbac_api_metrics'),
    path('rbac/dashboard/', getattr(views, 'RBACDashboardView', getattr(views, 'RBACListView')).as_view(), name='rbac_dashboard'),
    path('rbac/analytics/', getattr(views, 'RBACAnalyticsView', getattr(views, 'RBACListView')).as_view(), name='rbac_analytics'),
]

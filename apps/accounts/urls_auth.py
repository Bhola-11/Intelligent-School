"""URL Routing for EduFlow Authentication Workflows & Profile Management (Auth)."""
from django.urls import path
try:
    from . import views_auth as views
except ImportError:
    from . import views

app_name = 'accounts'

urlpatterns = [
    path('auth/', getattr(views, 'AuthListView').as_view(), name='auth_list'),
    path('auth/create/', getattr(views, 'AuthCreateView').as_view(), name='auth_create'),
    path('auth/<int:pk>/', getattr(views, 'AuthDetailView').as_view(), name='auth_detail'),
    path('auth/<int:pk>/edit/', getattr(views, 'AuthUpdateView').as_view(), name='auth_edit'),
    path('auth/<int:pk>/delete/', getattr(views, 'AuthDeleteView').as_view(), name='auth_delete'),
    path('auth/<int:master_pk>/add-item/', getattr(views, 'AuthItemCreateView').as_view(), name='auth_add_item'),
    path('auth/<int:master_pk>/allocate/', getattr(views, 'AuthAllocationCreateView').as_view(), name='auth_allocate'),
    path('auth/bulk-update/', getattr(views, 'AuthBulkStatusUpdateView').as_view(), name='auth_bulk_update'),
    path('auth/export/csv/', getattr(views, 'AuthExportCSVView').as_view(), name='auth_export_csv'),
    path('auth/export/json/', getattr(views, 'AuthExportJSONView').as_view(), name='auth_export_json'),
    path('auth/api/list/', getattr(views, 'AuthAPIListView').as_view(), name='auth_api_list'),
    path('auth/<int:pk>/api/metrics/', getattr(views, 'AuthAPIMetricsView').as_view(), name='auth_api_metrics'),
    path('auth/dashboard/', getattr(views, 'AuthDashboardView', getattr(views, 'AuthListView')).as_view(), name='auth_dashboard'),
    path('auth/analytics/', getattr(views, 'AuthAnalyticsView', getattr(views, 'AuthListView')).as_view(), name='auth_analytics'),
]

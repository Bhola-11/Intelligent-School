"""URL Routing for EduFlow Student Medical & Health Records (Health)."""
from django.urls import path
try:
    from . import views_health as views
except ImportError:
    from . import views

app_name = 'students'

urlpatterns = [
    path('health/', getattr(views, 'HealthListView').as_view(), name='health_list'),
    path('health/create/', getattr(views, 'HealthCreateView').as_view(), name='health_create'),
    path('health/<int:pk>/', getattr(views, 'HealthDetailView').as_view(), name='health_detail'),
    path('health/<int:pk>/edit/', getattr(views, 'HealthUpdateView').as_view(), name='health_edit'),
    path('health/<int:pk>/delete/', getattr(views, 'HealthDeleteView').as_view(), name='health_delete'),
    path('health/<int:master_pk>/add-item/', getattr(views, 'HealthItemCreateView').as_view(), name='health_add_item'),
    path('health/<int:master_pk>/allocate/', getattr(views, 'HealthAllocationCreateView').as_view(), name='health_allocate'),
    path('health/bulk-update/', getattr(views, 'HealthBulkStatusUpdateView').as_view(), name='health_bulk_update'),
    path('health/export/csv/', getattr(views, 'HealthExportCSVView').as_view(), name='health_export_csv'),
    path('health/export/json/', getattr(views, 'HealthExportJSONView').as_view(), name='health_export_json'),
    path('health/api/list/', getattr(views, 'HealthAPIListView').as_view(), name='health_api_list'),
    path('health/<int:pk>/api/metrics/', getattr(views, 'HealthAPIMetricsView').as_view(), name='health_api_metrics'),
    path('health/dashboard/', getattr(views, 'HealthDashboardView', getattr(views, 'HealthListView')).as_view(), name='health_dashboard'),
    path('health/analytics/', getattr(views, 'HealthAnalyticsView', getattr(views, 'HealthListView')).as_view(), name='health_analytics'),
]

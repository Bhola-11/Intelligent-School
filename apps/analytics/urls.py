"""URL Routing for EduFlow Student Academic Performance Trends (Performance)."""
from django.urls import path
try:
    from . import views_performance as views
except ImportError:
    from . import views

app_name = 'analytics'

urlpatterns = [
    path('performance/', getattr(views, 'PerformanceListView').as_view(), name='performance_list'),
    path('performance/create/', getattr(views, 'PerformanceCreateView').as_view(), name='performance_create'),
    path('performance/<int:pk>/', getattr(views, 'PerformanceDetailView').as_view(), name='performance_detail'),
    path('performance/<int:pk>/edit/', getattr(views, 'PerformanceUpdateView').as_view(), name='performance_edit'),
    path('performance/<int:pk>/delete/', getattr(views, 'PerformanceDeleteView').as_view(), name='performance_delete'),
    path('performance/<int:master_pk>/add-item/', getattr(views, 'PerformanceItemCreateView').as_view(), name='performance_add_item'),
    path('performance/<int:master_pk>/allocate/', getattr(views, 'PerformanceAllocationCreateView').as_view(), name='performance_allocate'),
    path('performance/bulk-update/', getattr(views, 'PerformanceBulkStatusUpdateView').as_view(), name='performance_bulk_update'),
    path('performance/export/csv/', getattr(views, 'PerformanceExportCSVView').as_view(), name='performance_export_csv'),
    path('performance/export/json/', getattr(views, 'PerformanceExportJSONView').as_view(), name='performance_export_json'),
    path('performance/api/list/', getattr(views, 'PerformanceAPIListView').as_view(), name='performance_api_list'),
    path('performance/<int:pk>/api/metrics/', getattr(views, 'PerformanceAPIMetricsView').as_view(), name='performance_api_metrics'),
    path('performance/dashboard/', getattr(views, 'PerformanceDashboardView', getattr(views, 'PerformanceListView')).as_view(), name='performance_dashboard'),
    path('performance/analytics/', getattr(views, 'PerformanceAnalyticsView', getattr(views, 'PerformanceListView')).as_view(), name='performance_analytics'),
]

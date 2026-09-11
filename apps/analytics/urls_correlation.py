"""URL Routing for EduFlow Attendance Correlation & At-Risk Predictor (Correlation)."""
from django.urls import path
try:
    from . import views_correlation as views
except ImportError:
    from . import views

app_name = 'analytics'

urlpatterns = [
    path('correlation/', getattr(views, 'CorrelationListView').as_view(), name='correlation_list'),
    path('correlation/create/', getattr(views, 'CorrelationCreateView').as_view(), name='correlation_create'),
    path('correlation/<int:pk>/', getattr(views, 'CorrelationDetailView').as_view(), name='correlation_detail'),
    path('correlation/<int:pk>/edit/', getattr(views, 'CorrelationUpdateView').as_view(), name='correlation_edit'),
    path('correlation/<int:pk>/delete/', getattr(views, 'CorrelationDeleteView').as_view(), name='correlation_delete'),
    path('correlation/<int:master_pk>/add-item/', getattr(views, 'CorrelationItemCreateView').as_view(), name='correlation_add_item'),
    path('correlation/<int:master_pk>/allocate/', getattr(views, 'CorrelationAllocationCreateView').as_view(), name='correlation_allocate'),
    path('correlation/bulk-update/', getattr(views, 'CorrelationBulkStatusUpdateView').as_view(), name='correlation_bulk_update'),
    path('correlation/export/csv/', getattr(views, 'CorrelationExportCSVView').as_view(), name='correlation_export_csv'),
    path('correlation/export/json/', getattr(views, 'CorrelationExportJSONView').as_view(), name='correlation_export_json'),
    path('correlation/api/list/', getattr(views, 'CorrelationAPIListView').as_view(), name='correlation_api_list'),
    path('correlation/<int:pk>/api/metrics/', getattr(views, 'CorrelationAPIMetricsView').as_view(), name='correlation_api_metrics'),
    path('correlation/dashboard/', getattr(views, 'CorrelationDashboardView', getattr(views, 'CorrelationListView')).as_view(), name='correlation_dashboard'),
    path('correlation/analytics/', getattr(views, 'CorrelationAnalyticsView', getattr(views, 'CorrelationListView')).as_view(), name='correlation_analytics'),
]

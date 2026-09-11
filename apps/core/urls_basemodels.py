"""URL Routing for EduFlow Core Base Models & Model Mixins (BaseModels)."""
from django.urls import path
try:
    from . import views_basemodels as views
except ImportError:
    from . import views

app_name = 'core'

urlpatterns = [
    path('basemodels/', getattr(views, 'BaseModelsListView').as_view(), name='basemodels_list'),
    path('basemodels/create/', getattr(views, 'BaseModelsCreateView').as_view(), name='basemodels_create'),
    path('basemodels/<int:pk>/', getattr(views, 'BaseModelsDetailView').as_view(), name='basemodels_detail'),
    path('basemodels/<int:pk>/edit/', getattr(views, 'BaseModelsUpdateView').as_view(), name='basemodels_edit'),
    path('basemodels/<int:pk>/delete/', getattr(views, 'BaseModelsDeleteView').as_view(), name='basemodels_delete'),
    path('basemodels/<int:master_pk>/add-item/', getattr(views, 'BaseModelsItemCreateView').as_view(), name='basemodels_add_item'),
    path('basemodels/<int:master_pk>/allocate/', getattr(views, 'BaseModelsAllocationCreateView').as_view(), name='basemodels_allocate'),
    path('basemodels/bulk-update/', getattr(views, 'BaseModelsBulkStatusUpdateView').as_view(), name='basemodels_bulk_update'),
    path('basemodels/export/csv/', getattr(views, 'BaseModelsExportCSVView').as_view(), name='basemodels_export_csv'),
    path('basemodels/export/json/', getattr(views, 'BaseModelsExportJSONView').as_view(), name='basemodels_export_json'),
    path('basemodels/api/list/', getattr(views, 'BaseModelsAPIListView').as_view(), name='basemodels_api_list'),
    path('basemodels/<int:pk>/api/metrics/', getattr(views, 'BaseModelsAPIMetricsView').as_view(), name='basemodels_api_metrics'),
    path('basemodels/dashboard/', getattr(views, 'BaseModelsDashboardView', getattr(views, 'BaseModelsListView')).as_view(), name='basemodels_dashboard'),
    path('basemodels/analytics/', getattr(views, 'BaseModelsAnalyticsView', getattr(views, 'BaseModelsListView')).as_view(), name='basemodels_analytics'),
]

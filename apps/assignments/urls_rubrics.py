"""URL Routing for EduFlow Assignment Attachments & Rubric Matrix (Rubrics)."""
from django.urls import path
try:
    from . import views_rubrics as views
except ImportError:
    from . import views

app_name = 'assignments'

urlpatterns = [
    path('rubrics/', getattr(views, 'RubricsListView').as_view(), name='rubrics_list'),
    path('rubrics/create/', getattr(views, 'RubricsCreateView').as_view(), name='rubrics_create'),
    path('rubrics/<int:pk>/', getattr(views, 'RubricsDetailView').as_view(), name='rubrics_detail'),
    path('rubrics/<int:pk>/edit/', getattr(views, 'RubricsUpdateView').as_view(), name='rubrics_edit'),
    path('rubrics/<int:pk>/delete/', getattr(views, 'RubricsDeleteView').as_view(), name='rubrics_delete'),
    path('rubrics/<int:master_pk>/add-item/', getattr(views, 'RubricsItemCreateView').as_view(), name='rubrics_add_item'),
    path('rubrics/<int:master_pk>/allocate/', getattr(views, 'RubricsAllocationCreateView').as_view(), name='rubrics_allocate'),
    path('rubrics/bulk-update/', getattr(views, 'RubricsBulkStatusUpdateView').as_view(), name='rubrics_bulk_update'),
    path('rubrics/export/csv/', getattr(views, 'RubricsExportCSVView').as_view(), name='rubrics_export_csv'),
    path('rubrics/export/json/', getattr(views, 'RubricsExportJSONView').as_view(), name='rubrics_export_json'),
    path('rubrics/api/list/', getattr(views, 'RubricsAPIListView').as_view(), name='rubrics_api_list'),
    path('rubrics/<int:pk>/api/metrics/', getattr(views, 'RubricsAPIMetricsView').as_view(), name='rubrics_api_metrics'),
    path('rubrics/dashboard/', getattr(views, 'RubricsDashboardView', getattr(views, 'RubricsListView')).as_view(), name='rubrics_dashboard'),
    path('rubrics/analytics/', getattr(views, 'RubricsAnalyticsView', getattr(views, 'RubricsListView')).as_view(), name='rubrics_analytics'),
]

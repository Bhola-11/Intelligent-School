"""URL Routing for EduFlow Report Card Custom Templates & Layouts (Templates)."""
from django.urls import path
try:
    from . import views_templates as views
except ImportError:
    from . import views

app_name = 'report_cards'

urlpatterns = [
    path('templates/', getattr(views, 'TemplatesListView').as_view(), name='templates_list'),
    path('templates/create/', getattr(views, 'TemplatesCreateView').as_view(), name='templates_create'),
    path('templates/<int:pk>/', getattr(views, 'TemplatesDetailView').as_view(), name='templates_detail'),
    path('templates/<int:pk>/edit/', getattr(views, 'TemplatesUpdateView').as_view(), name='templates_edit'),
    path('templates/<int:pk>/delete/', getattr(views, 'TemplatesDeleteView').as_view(), name='templates_delete'),
    path('templates/<int:master_pk>/add-item/', getattr(views, 'TemplatesItemCreateView').as_view(), name='templates_add_item'),
    path('templates/<int:master_pk>/allocate/', getattr(views, 'TemplatesAllocationCreateView').as_view(), name='templates_allocate'),
    path('templates/bulk-update/', getattr(views, 'TemplatesBulkStatusUpdateView').as_view(), name='templates_bulk_update'),
    path('templates/export/csv/', getattr(views, 'TemplatesExportCSVView').as_view(), name='templates_export_csv'),
    path('templates/export/json/', getattr(views, 'TemplatesExportJSONView').as_view(), name='templates_export_json'),
    path('templates/api/list/', getattr(views, 'TemplatesAPIListView').as_view(), name='templates_api_list'),
    path('templates/<int:pk>/api/metrics/', getattr(views, 'TemplatesAPIMetricsView').as_view(), name='templates_api_metrics'),
    path('templates/dashboard/', getattr(views, 'TemplatesDashboardView', getattr(views, 'TemplatesListView')).as_view(), name='templates_dashboard'),
    path('templates/analytics/', getattr(views, 'TemplatesAnalyticsView', getattr(views, 'TemplatesListView')).as_view(), name='templates_analytics'),
]

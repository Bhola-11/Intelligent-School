"""URL Routing for EduFlow Scholarships, Discounts & Late Fines (Concessions)."""
from django.urls import path
try:
    from . import views_concessions as views
except ImportError:
    from . import views

app_name = 'fees'

urlpatterns = [
    path('concessions/', getattr(views, 'ConcessionsListView').as_view(), name='concessions_list'),
    path('concessions/create/', getattr(views, 'ConcessionsCreateView').as_view(), name='concessions_create'),
    path('concessions/<int:pk>/', getattr(views, 'ConcessionsDetailView').as_view(), name='concessions_detail'),
    path('concessions/<int:pk>/edit/', getattr(views, 'ConcessionsUpdateView').as_view(), name='concessions_edit'),
    path('concessions/<int:pk>/delete/', getattr(views, 'ConcessionsDeleteView').as_view(), name='concessions_delete'),
    path('concessions/<int:master_pk>/add-item/', getattr(views, 'ConcessionsItemCreateView').as_view(), name='concessions_add_item'),
    path('concessions/<int:master_pk>/allocate/', getattr(views, 'ConcessionsAllocationCreateView').as_view(), name='concessions_allocate'),
    path('concessions/bulk-update/', getattr(views, 'ConcessionsBulkStatusUpdateView').as_view(), name='concessions_bulk_update'),
    path('concessions/export/csv/', getattr(views, 'ConcessionsExportCSVView').as_view(), name='concessions_export_csv'),
    path('concessions/export/json/', getattr(views, 'ConcessionsExportJSONView').as_view(), name='concessions_export_json'),
    path('concessions/api/list/', getattr(views, 'ConcessionsAPIListView').as_view(), name='concessions_api_list'),
    path('concessions/<int:pk>/api/metrics/', getattr(views, 'ConcessionsAPIMetricsView').as_view(), name='concessions_api_metrics'),
    path('concessions/dashboard/', getattr(views, 'ConcessionsDashboardView', getattr(views, 'ConcessionsListView')).as_view(), name='concessions_dashboard'),
    path('concessions/analytics/', getattr(views, 'ConcessionsAnalyticsView', getattr(views, 'ConcessionsListView')).as_view(), name='concessions_analytics'),
]

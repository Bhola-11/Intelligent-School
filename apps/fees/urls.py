"""URL Routing for EduFlow Fee Categories & Structure Configuration (FeeStructures)."""
from django.urls import path
try:
    from . import views_feestructures as views
except ImportError:
    from . import views

app_name = 'fees'

urlpatterns = [
    path('feestructures/', getattr(views, 'FeeStructuresListView').as_view(), name='feestructures_list'),
    path('feestructures/create/', getattr(views, 'FeeStructuresCreateView').as_view(), name='feestructures_create'),
    path('feestructures/<int:pk>/', getattr(views, 'FeeStructuresDetailView').as_view(), name='feestructures_detail'),
    path('feestructures/<int:pk>/edit/', getattr(views, 'FeeStructuresUpdateView').as_view(), name='feestructures_edit'),
    path('feestructures/<int:pk>/delete/', getattr(views, 'FeeStructuresDeleteView').as_view(), name='feestructures_delete'),
    path('feestructures/<int:master_pk>/add-item/', getattr(views, 'FeeStructuresItemCreateView').as_view(), name='feestructures_add_item'),
    path('feestructures/<int:master_pk>/allocate/', getattr(views, 'FeeStructuresAllocationCreateView').as_view(), name='feestructures_allocate'),
    path('feestructures/bulk-update/', getattr(views, 'FeeStructuresBulkStatusUpdateView').as_view(), name='feestructures_bulk_update'),
    path('feestructures/export/csv/', getattr(views, 'FeeStructuresExportCSVView').as_view(), name='feestructures_export_csv'),
    path('feestructures/export/json/', getattr(views, 'FeeStructuresExportJSONView').as_view(), name='feestructures_export_json'),
    path('feestructures/api/list/', getattr(views, 'FeeStructuresAPIListView').as_view(), name='feestructures_api_list'),
    path('feestructures/<int:pk>/api/metrics/', getattr(views, 'FeeStructuresAPIMetricsView').as_view(), name='feestructures_api_metrics'),
    path('feestructures/dashboard/', getattr(views, 'FeeStructuresDashboardView', getattr(views, 'FeeStructuresListView')).as_view(), name='feestructures_dashboard'),
    path('feestructures/analytics/', getattr(views, 'FeeStructuresAnalyticsView', getattr(views, 'FeeStructuresListView')).as_view(), name='feestructures_analytics'),
]

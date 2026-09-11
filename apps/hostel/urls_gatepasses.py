"""URL Routing for EduFlow Hostel Gate Passes & Resident Discipline (GatePasses)."""
from django.urls import path
try:
    from . import views_gatepasses as views
except ImportError:
    from . import views

app_name = 'hostel'

urlpatterns = [
    path('gatepasses/', getattr(views, 'GatePassesListView').as_view(), name='gatepasses_list'),
    path('gatepasses/create/', getattr(views, 'GatePassesCreateView').as_view(), name='gatepasses_create'),
    path('gatepasses/<int:pk>/', getattr(views, 'GatePassesDetailView').as_view(), name='gatepasses_detail'),
    path('gatepasses/<int:pk>/edit/', getattr(views, 'GatePassesUpdateView').as_view(), name='gatepasses_edit'),
    path('gatepasses/<int:pk>/delete/', getattr(views, 'GatePassesDeleteView').as_view(), name='gatepasses_delete'),
    path('gatepasses/<int:master_pk>/add-item/', getattr(views, 'GatePassesItemCreateView').as_view(), name='gatepasses_add_item'),
    path('gatepasses/<int:master_pk>/allocate/', getattr(views, 'GatePassesAllocationCreateView').as_view(), name='gatepasses_allocate'),
    path('gatepasses/bulk-update/', getattr(views, 'GatePassesBulkStatusUpdateView').as_view(), name='gatepasses_bulk_update'),
    path('gatepasses/export/csv/', getattr(views, 'GatePassesExportCSVView').as_view(), name='gatepasses_export_csv'),
    path('gatepasses/export/json/', getattr(views, 'GatePassesExportJSONView').as_view(), name='gatepasses_export_json'),
    path('gatepasses/api/list/', getattr(views, 'GatePassesAPIListView').as_view(), name='gatepasses_api_list'),
    path('gatepasses/<int:pk>/api/metrics/', getattr(views, 'GatePassesAPIMetricsView').as_view(), name='gatepasses_api_metrics'),
    path('gatepasses/dashboard/', getattr(views, 'GatePassesDashboardView', getattr(views, 'GatePassesListView')).as_view(), name='gatepasses_dashboard'),
    path('gatepasses/analytics/', getattr(views, 'GatePassesAnalyticsView', getattr(views, 'GatePassesListView')).as_view(), name='gatepasses_analytics'),
]

"""URL Routing for EduFlow Timetable Conflict Detection Engine (ConflictEngine)."""
from django.urls import path
try:
    from . import views_conflictengine as views
except ImportError:
    from . import views

app_name = 'timetable'

urlpatterns = [
    path('conflictengine/', getattr(views, 'ConflictEngineListView').as_view(), name='conflictengine_list'),
    path('conflictengine/create/', getattr(views, 'ConflictEngineCreateView').as_view(), name='conflictengine_create'),
    path('conflictengine/<int:pk>/', getattr(views, 'ConflictEngineDetailView').as_view(), name='conflictengine_detail'),
    path('conflictengine/<int:pk>/edit/', getattr(views, 'ConflictEngineUpdateView').as_view(), name='conflictengine_edit'),
    path('conflictengine/<int:pk>/delete/', getattr(views, 'ConflictEngineDeleteView').as_view(), name='conflictengine_delete'),
    path('conflictengine/<int:master_pk>/add-item/', getattr(views, 'ConflictEngineItemCreateView').as_view(), name='conflictengine_add_item'),
    path('conflictengine/<int:master_pk>/allocate/', getattr(views, 'ConflictEngineAllocationCreateView').as_view(), name='conflictengine_allocate'),
    path('conflictengine/bulk-update/', getattr(views, 'ConflictEngineBulkStatusUpdateView').as_view(), name='conflictengine_bulk_update'),
    path('conflictengine/export/csv/', getattr(views, 'ConflictEngineExportCSVView').as_view(), name='conflictengine_export_csv'),
    path('conflictengine/export/json/', getattr(views, 'ConflictEngineExportJSONView').as_view(), name='conflictengine_export_json'),
    path('conflictengine/api/list/', getattr(views, 'ConflictEngineAPIListView').as_view(), name='conflictengine_api_list'),
    path('conflictengine/<int:pk>/api/metrics/', getattr(views, 'ConflictEngineAPIMetricsView').as_view(), name='conflictengine_api_metrics'),
    path('conflictengine/dashboard/', getattr(views, 'ConflictEngineDashboardView', getattr(views, 'ConflictEngineListView')).as_view(), name='conflictengine_dashboard'),
    path('conflictengine/analytics/', getattr(views, 'ConflictEngineAnalyticsView', getattr(views, 'ConflictEngineListView')).as_view(), name='conflictengine_analytics'),
]

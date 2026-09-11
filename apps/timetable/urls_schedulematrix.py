"""URL Routing for EduFlow Timetable Schedule Matrix & Substitution (ScheduleMatrix)."""
from django.urls import path
try:
    from . import views_schedulematrix as views
except ImportError:
    from . import views

app_name = 'timetable'

urlpatterns = [
    path('schedulematrix/', getattr(views, 'ScheduleMatrixListView').as_view(), name='schedulematrix_list'),
    path('schedulematrix/create/', getattr(views, 'ScheduleMatrixCreateView').as_view(), name='schedulematrix_create'),
    path('schedulematrix/<int:pk>/', getattr(views, 'ScheduleMatrixDetailView').as_view(), name='schedulematrix_detail'),
    path('schedulematrix/<int:pk>/edit/', getattr(views, 'ScheduleMatrixUpdateView').as_view(), name='schedulematrix_edit'),
    path('schedulematrix/<int:pk>/delete/', getattr(views, 'ScheduleMatrixDeleteView').as_view(), name='schedulematrix_delete'),
    path('schedulematrix/<int:master_pk>/add-item/', getattr(views, 'ScheduleMatrixItemCreateView').as_view(), name='schedulematrix_add_item'),
    path('schedulematrix/<int:master_pk>/allocate/', getattr(views, 'ScheduleMatrixAllocationCreateView').as_view(), name='schedulematrix_allocate'),
    path('schedulematrix/bulk-update/', getattr(views, 'ScheduleMatrixBulkStatusUpdateView').as_view(), name='schedulematrix_bulk_update'),
    path('schedulematrix/export/csv/', getattr(views, 'ScheduleMatrixExportCSVView').as_view(), name='schedulematrix_export_csv'),
    path('schedulematrix/export/json/', getattr(views, 'ScheduleMatrixExportJSONView').as_view(), name='schedulematrix_export_json'),
    path('schedulematrix/api/list/', getattr(views, 'ScheduleMatrixAPIListView').as_view(), name='schedulematrix_api_list'),
    path('schedulematrix/<int:pk>/api/metrics/', getattr(views, 'ScheduleMatrixAPIMetricsView').as_view(), name='schedulematrix_api_metrics'),
    path('schedulematrix/dashboard/', getattr(views, 'ScheduleMatrixDashboardView', getattr(views, 'ScheduleMatrixListView')).as_view(), name='schedulematrix_dashboard'),
    path('schedulematrix/analytics/', getattr(views, 'ScheduleMatrixAnalyticsView', getattr(views, 'ScheduleMatrixListView')).as_view(), name='schedulematrix_analytics'),
]

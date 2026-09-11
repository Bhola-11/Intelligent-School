"""URL Routing for EduFlow Grading Schemes & Grade Scale Boundaries (GradeScales)."""
from django.urls import path
try:
    from . import views_gradescales as views
except ImportError:
    from . import views

app_name = 'grading'

urlpatterns = [
    path('gradescales/', getattr(views, 'GradeScalesListView').as_view(), name='gradescales_list'),
    path('gradescales/create/', getattr(views, 'GradeScalesCreateView').as_view(), name='gradescales_create'),
    path('gradescales/<int:pk>/', getattr(views, 'GradeScalesDetailView').as_view(), name='gradescales_detail'),
    path('gradescales/<int:pk>/edit/', getattr(views, 'GradeScalesUpdateView').as_view(), name='gradescales_edit'),
    path('gradescales/<int:pk>/delete/', getattr(views, 'GradeScalesDeleteView').as_view(), name='gradescales_delete'),
    path('gradescales/<int:master_pk>/add-item/', getattr(views, 'GradeScalesItemCreateView').as_view(), name='gradescales_add_item'),
    path('gradescales/<int:master_pk>/allocate/', getattr(views, 'GradeScalesAllocationCreateView').as_view(), name='gradescales_allocate'),
    path('gradescales/bulk-update/', getattr(views, 'GradeScalesBulkStatusUpdateView').as_view(), name='gradescales_bulk_update'),
    path('gradescales/export/csv/', getattr(views, 'GradeScalesExportCSVView').as_view(), name='gradescales_export_csv'),
    path('gradescales/export/json/', getattr(views, 'GradeScalesExportJSONView').as_view(), name='gradescales_export_json'),
    path('gradescales/api/list/', getattr(views, 'GradeScalesAPIListView').as_view(), name='gradescales_api_list'),
    path('gradescales/<int:pk>/api/metrics/', getattr(views, 'GradeScalesAPIMetricsView').as_view(), name='gradescales_api_metrics'),
    path('gradescales/dashboard/', getattr(views, 'GradeScalesDashboardView', getattr(views, 'GradeScalesListView')).as_view(), name='gradescales_dashboard'),
    path('gradescales/analytics/', getattr(views, 'GradeScalesAnalyticsView', getattr(views, 'GradeScalesListView')).as_view(), name='gradescales_analytics'),
]

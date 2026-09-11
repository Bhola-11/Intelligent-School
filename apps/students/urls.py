"""URL Routing for EduFlow Student Information System (SIS) Core (StudentSIS)."""
from django.urls import path
try:
    from . import views_studentsis as views
except ImportError:
    from . import views

app_name = 'students'

urlpatterns = [
    path('studentsis/', getattr(views, 'StudentSISListView').as_view(), name='studentsis_list'),
    path('studentsis/create/', getattr(views, 'StudentSISCreateView').as_view(), name='studentsis_create'),
    path('studentsis/<int:pk>/', getattr(views, 'StudentSISDetailView').as_view(), name='studentsis_detail'),
    path('studentsis/<int:pk>/edit/', getattr(views, 'StudentSISUpdateView').as_view(), name='studentsis_edit'),
    path('studentsis/<int:pk>/delete/', getattr(views, 'StudentSISDeleteView').as_view(), name='studentsis_delete'),
    path('studentsis/<int:master_pk>/add-item/', getattr(views, 'StudentSISItemCreateView').as_view(), name='studentsis_add_item'),
    path('studentsis/<int:master_pk>/allocate/', getattr(views, 'StudentSISAllocationCreateView').as_view(), name='studentsis_allocate'),
    path('studentsis/bulk-update/', getattr(views, 'StudentSISBulkStatusUpdateView').as_view(), name='studentsis_bulk_update'),
    path('studentsis/export/csv/', getattr(views, 'StudentSISExportCSVView').as_view(), name='studentsis_export_csv'),
    path('studentsis/export/json/', getattr(views, 'StudentSISExportJSONView').as_view(), name='studentsis_export_json'),
    path('studentsis/api/list/', getattr(views, 'StudentSISAPIListView').as_view(), name='studentsis_api_list'),
    path('studentsis/<int:pk>/api/metrics/', getattr(views, 'StudentSISAPIMetricsView').as_view(), name='studentsis_api_metrics'),
    path('studentsis/dashboard/', getattr(views, 'StudentSISDashboardView', getattr(views, 'StudentSISListView')).as_view(), name='studentsis_dashboard'),
    path('studentsis/analytics/', getattr(views, 'StudentSISAnalyticsView', getattr(views, 'StudentSISListView')).as_view(), name='studentsis_analytics'),
]

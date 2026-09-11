"""URL Routing for EduFlow Examination Coordinator Suite (ExamDesk)."""
from django.urls import path
try:
    from . import views_examdesk as views
except ImportError:
    from . import views

app_name = 'portals'

urlpatterns = [
    path('examdesk/', getattr(views, 'ExamDeskListView').as_view(), name='examdesk_list'),
    path('examdesk/create/', getattr(views, 'ExamDeskCreateView').as_view(), name='examdesk_create'),
    path('examdesk/<int:pk>/', getattr(views, 'ExamDeskDetailView').as_view(), name='examdesk_detail'),
    path('examdesk/<int:pk>/edit/', getattr(views, 'ExamDeskUpdateView').as_view(), name='examdesk_edit'),
    path('examdesk/<int:pk>/delete/', getattr(views, 'ExamDeskDeleteView').as_view(), name='examdesk_delete'),
    path('examdesk/<int:master_pk>/add-item/', getattr(views, 'ExamDeskItemCreateView').as_view(), name='examdesk_add_item'),
    path('examdesk/<int:master_pk>/allocate/', getattr(views, 'ExamDeskAllocationCreateView').as_view(), name='examdesk_allocate'),
    path('examdesk/bulk-update/', getattr(views, 'ExamDeskBulkStatusUpdateView').as_view(), name='examdesk_bulk_update'),
    path('examdesk/export/csv/', getattr(views, 'ExamDeskExportCSVView').as_view(), name='examdesk_export_csv'),
    path('examdesk/export/json/', getattr(views, 'ExamDeskExportJSONView').as_view(), name='examdesk_export_json'),
    path('examdesk/api/list/', getattr(views, 'ExamDeskAPIListView').as_view(), name='examdesk_api_list'),
    path('examdesk/<int:pk>/api/metrics/', getattr(views, 'ExamDeskAPIMetricsView').as_view(), name='examdesk_api_metrics'),
    path('examdesk/dashboard/', getattr(views, 'ExamDeskDashboardView', getattr(views, 'ExamDeskListView')).as_view(), name='examdesk_dashboard'),
    path('examdesk/analytics/', getattr(views, 'ExamDeskAnalyticsView', getattr(views, 'ExamDeskListView')).as_view(), name='examdesk_analytics'),
]

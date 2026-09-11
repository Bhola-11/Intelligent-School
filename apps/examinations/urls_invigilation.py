"""URL Routing for EduFlow Exam Rooms & Invigilator Assignments (Invigilation)."""
from django.urls import path
try:
    from . import views_invigilation as views
except ImportError:
    from . import views

app_name = 'examinations'

urlpatterns = [
    path('invigilation/', getattr(views, 'InvigilationListView').as_view(), name='invigilation_list'),
    path('invigilation/create/', getattr(views, 'InvigilationCreateView').as_view(), name='invigilation_create'),
    path('invigilation/<int:pk>/', getattr(views, 'InvigilationDetailView').as_view(), name='invigilation_detail'),
    path('invigilation/<int:pk>/edit/', getattr(views, 'InvigilationUpdateView').as_view(), name='invigilation_edit'),
    path('invigilation/<int:pk>/delete/', getattr(views, 'InvigilationDeleteView').as_view(), name='invigilation_delete'),
    path('invigilation/<int:master_pk>/add-item/', getattr(views, 'InvigilationItemCreateView').as_view(), name='invigilation_add_item'),
    path('invigilation/<int:master_pk>/allocate/', getattr(views, 'InvigilationAllocationCreateView').as_view(), name='invigilation_allocate'),
    path('invigilation/bulk-update/', getattr(views, 'InvigilationBulkStatusUpdateView').as_view(), name='invigilation_bulk_update'),
    path('invigilation/export/csv/', getattr(views, 'InvigilationExportCSVView').as_view(), name='invigilation_export_csv'),
    path('invigilation/export/json/', getattr(views, 'InvigilationExportJSONView').as_view(), name='invigilation_export_json'),
    path('invigilation/api/list/', getattr(views, 'InvigilationAPIListView').as_view(), name='invigilation_api_list'),
    path('invigilation/<int:pk>/api/metrics/', getattr(views, 'InvigilationAPIMetricsView').as_view(), name='invigilation_api_metrics'),
    path('invigilation/dashboard/', getattr(views, 'InvigilationDashboardView', getattr(views, 'InvigilationListView')).as_view(), name='invigilation_dashboard'),
    path('invigilation/analytics/', getattr(views, 'InvigilationAnalyticsView', getattr(views, 'InvigilationListView')).as_view(), name='invigilation_analytics'),
]

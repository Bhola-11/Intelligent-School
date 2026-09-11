"""URL Routing for EduFlow Online Admissions Application Pipeline (Applications)."""
from django.urls import path
try:
    from . import views_applications as views
except ImportError:
    from . import views

app_name = 'admissions'

urlpatterns = [
    path('applications/', getattr(views, 'ApplicationsListView').as_view(), name='applications_list'),
    path('applications/create/', getattr(views, 'ApplicationsCreateView').as_view(), name='applications_create'),
    path('applications/<int:pk>/', getattr(views, 'ApplicationsDetailView').as_view(), name='applications_detail'),
    path('applications/<int:pk>/edit/', getattr(views, 'ApplicationsUpdateView').as_view(), name='applications_edit'),
    path('applications/<int:pk>/delete/', getattr(views, 'ApplicationsDeleteView').as_view(), name='applications_delete'),
    path('applications/<int:master_pk>/add-item/', getattr(views, 'ApplicationsItemCreateView').as_view(), name='applications_add_item'),
    path('applications/<int:master_pk>/allocate/', getattr(views, 'ApplicationsAllocationCreateView').as_view(), name='applications_allocate'),
    path('applications/bulk-update/', getattr(views, 'ApplicationsBulkStatusUpdateView').as_view(), name='applications_bulk_update'),
    path('applications/export/csv/', getattr(views, 'ApplicationsExportCSVView').as_view(), name='applications_export_csv'),
    path('applications/export/json/', getattr(views, 'ApplicationsExportJSONView').as_view(), name='applications_export_json'),
    path('applications/api/list/', getattr(views, 'ApplicationsAPIListView').as_view(), name='applications_api_list'),
    path('applications/<int:pk>/api/metrics/', getattr(views, 'ApplicationsAPIMetricsView').as_view(), name='applications_api_metrics'),
    path('applications/dashboard/', getattr(views, 'ApplicationsDashboardView', getattr(views, 'ApplicationsListView')).as_view(), name='applications_dashboard'),
    path('applications/analytics/', getattr(views, 'ApplicationsAnalyticsView', getattr(views, 'ApplicationsListView')).as_view(), name='applications_analytics'),
]

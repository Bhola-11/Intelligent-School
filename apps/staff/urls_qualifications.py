"""URL Routing for EduFlow Staff Qualifications, Degrees & Certifications (Qualifications)."""
from django.urls import path
try:
    from . import views_qualifications as views
except ImportError:
    from . import views

app_name = 'staff'

urlpatterns = [
    path('qualifications/', getattr(views, 'QualificationsListView').as_view(), name='qualifications_list'),
    path('qualifications/create/', getattr(views, 'QualificationsCreateView').as_view(), name='qualifications_create'),
    path('qualifications/<int:pk>/', getattr(views, 'QualificationsDetailView').as_view(), name='qualifications_detail'),
    path('qualifications/<int:pk>/edit/', getattr(views, 'QualificationsUpdateView').as_view(), name='qualifications_edit'),
    path('qualifications/<int:pk>/delete/', getattr(views, 'QualificationsDeleteView').as_view(), name='qualifications_delete'),
    path('qualifications/<int:master_pk>/add-item/', getattr(views, 'QualificationsItemCreateView').as_view(), name='qualifications_add_item'),
    path('qualifications/<int:master_pk>/allocate/', getattr(views, 'QualificationsAllocationCreateView').as_view(), name='qualifications_allocate'),
    path('qualifications/bulk-update/', getattr(views, 'QualificationsBulkStatusUpdateView').as_view(), name='qualifications_bulk_update'),
    path('qualifications/export/csv/', getattr(views, 'QualificationsExportCSVView').as_view(), name='qualifications_export_csv'),
    path('qualifications/export/json/', getattr(views, 'QualificationsExportJSONView').as_view(), name='qualifications_export_json'),
    path('qualifications/api/list/', getattr(views, 'QualificationsAPIListView').as_view(), name='qualifications_api_list'),
    path('qualifications/<int:pk>/api/metrics/', getattr(views, 'QualificationsAPIMetricsView').as_view(), name='qualifications_api_metrics'),
    path('qualifications/dashboard/', getattr(views, 'QualificationsDashboardView', getattr(views, 'QualificationsListView')).as_view(), name='qualifications_dashboard'),
    path('qualifications/analytics/', getattr(views, 'QualificationsAnalyticsView', getattr(views, 'QualificationsListView')).as_view(), name='qualifications_analytics'),
]

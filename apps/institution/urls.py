"""URL Routing for EduFlow Institution Profile & Multi-Campus Architecture (Institution)."""
from django.urls import path
try:
    from . import views_institution as views
except ImportError:
    from . import views

app_name = 'institution'

urlpatterns = [
    path('institution/', getattr(views, 'InstitutionListView').as_view(), name='institution_list'),
    path('institution/create/', getattr(views, 'InstitutionCreateView').as_view(), name='institution_create'),
    path('institution/<int:pk>/', getattr(views, 'InstitutionDetailView').as_view(), name='institution_detail'),
    path('institution/<int:pk>/edit/', getattr(views, 'InstitutionUpdateView').as_view(), name='institution_edit'),
    path('institution/<int:pk>/delete/', getattr(views, 'InstitutionDeleteView').as_view(), name='institution_delete'),
    path('institution/<int:master_pk>/add-item/', getattr(views, 'InstitutionItemCreateView').as_view(), name='institution_add_item'),
    path('institution/<int:master_pk>/allocate/', getattr(views, 'InstitutionAllocationCreateView').as_view(), name='institution_allocate'),
    path('institution/bulk-update/', getattr(views, 'InstitutionBulkStatusUpdateView').as_view(), name='institution_bulk_update'),
    path('institution/export/csv/', getattr(views, 'InstitutionExportCSVView').as_view(), name='institution_export_csv'),
    path('institution/export/json/', getattr(views, 'InstitutionExportJSONView').as_view(), name='institution_export_json'),
    path('institution/api/list/', getattr(views, 'InstitutionAPIListView').as_view(), name='institution_api_list'),
    path('institution/<int:pk>/api/metrics/', getattr(views, 'InstitutionAPIMetricsView').as_view(), name='institution_api_metrics'),
    path('institution/dashboard/', getattr(views, 'InstitutionDashboardView', getattr(views, 'InstitutionListView')).as_view(), name='institution_dashboard'),
    path('institution/analytics/', getattr(views, 'InstitutionAnalyticsView', getattr(views, 'InstitutionListView')).as_view(), name='institution_analytics'),
]

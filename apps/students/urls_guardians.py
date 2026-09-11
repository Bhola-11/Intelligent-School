"""URL Routing for EduFlow Guardians, Parents & Emergency Contacts (Guardians)."""
from django.urls import path
try:
    from . import views_guardians as views
except ImportError:
    from . import views

app_name = 'students'

urlpatterns = [
    path('guardians/', getattr(views, 'GuardiansListView').as_view(), name='guardians_list'),
    path('guardians/create/', getattr(views, 'GuardiansCreateView').as_view(), name='guardians_create'),
    path('guardians/<int:pk>/', getattr(views, 'GuardiansDetailView').as_view(), name='guardians_detail'),
    path('guardians/<int:pk>/edit/', getattr(views, 'GuardiansUpdateView').as_view(), name='guardians_edit'),
    path('guardians/<int:pk>/delete/', getattr(views, 'GuardiansDeleteView').as_view(), name='guardians_delete'),
    path('guardians/<int:master_pk>/add-item/', getattr(views, 'GuardiansItemCreateView').as_view(), name='guardians_add_item'),
    path('guardians/<int:master_pk>/allocate/', getattr(views, 'GuardiansAllocationCreateView').as_view(), name='guardians_allocate'),
    path('guardians/bulk-update/', getattr(views, 'GuardiansBulkStatusUpdateView').as_view(), name='guardians_bulk_update'),
    path('guardians/export/csv/', getattr(views, 'GuardiansExportCSVView').as_view(), name='guardians_export_csv'),
    path('guardians/export/json/', getattr(views, 'GuardiansExportJSONView').as_view(), name='guardians_export_json'),
    path('guardians/api/list/', getattr(views, 'GuardiansAPIListView').as_view(), name='guardians_api_list'),
    path('guardians/<int:pk>/api/metrics/', getattr(views, 'GuardiansAPIMetricsView').as_view(), name='guardians_api_metrics'),
    path('guardians/dashboard/', getattr(views, 'GuardiansDashboardView', getattr(views, 'GuardiansListView')).as_view(), name='guardians_dashboard'),
    path('guardians/analytics/', getattr(views, 'GuardiansAnalyticsView', getattr(views, 'GuardiansListView')).as_view(), name='guardians_analytics'),
]

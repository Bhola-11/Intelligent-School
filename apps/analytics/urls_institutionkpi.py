"""URL Routing for EduFlow Institutional KPI & Executive Metrics (InstitutionKPI)."""
from django.urls import path
try:
    from . import views_institutionkpi as views
except ImportError:
    from . import views

app_name = 'analytics'

urlpatterns = [
    path('institutionkpi/', getattr(views, 'InstitutionKPIListView').as_view(), name='institutionkpi_list'),
    path('institutionkpi/create/', getattr(views, 'InstitutionKPICreateView').as_view(), name='institutionkpi_create'),
    path('institutionkpi/<int:pk>/', getattr(views, 'InstitutionKPIDetailView').as_view(), name='institutionkpi_detail'),
    path('institutionkpi/<int:pk>/edit/', getattr(views, 'InstitutionKPIUpdateView').as_view(), name='institutionkpi_edit'),
    path('institutionkpi/<int:pk>/delete/', getattr(views, 'InstitutionKPIDeleteView').as_view(), name='institutionkpi_delete'),
    path('institutionkpi/<int:master_pk>/add-item/', getattr(views, 'InstitutionKPIItemCreateView').as_view(), name='institutionkpi_add_item'),
    path('institutionkpi/<int:master_pk>/allocate/', getattr(views, 'InstitutionKPIAllocationCreateView').as_view(), name='institutionkpi_allocate'),
    path('institutionkpi/bulk-update/', getattr(views, 'InstitutionKPIBulkStatusUpdateView').as_view(), name='institutionkpi_bulk_update'),
    path('institutionkpi/export/csv/', getattr(views, 'InstitutionKPIExportCSVView').as_view(), name='institutionkpi_export_csv'),
    path('institutionkpi/export/json/', getattr(views, 'InstitutionKPIExportJSONView').as_view(), name='institutionkpi_export_json'),
    path('institutionkpi/api/list/', getattr(views, 'InstitutionKPIAPIListView').as_view(), name='institutionkpi_api_list'),
    path('institutionkpi/<int:pk>/api/metrics/', getattr(views, 'InstitutionKPIAPIMetricsView').as_view(), name='institutionkpi_api_metrics'),
    path('institutionkpi/dashboard/', getattr(views, 'InstitutionKPIDashboardView', getattr(views, 'InstitutionKPIListView')).as_view(), name='institutionkpi_dashboard'),
    path('institutionkpi/analytics/', getattr(views, 'InstitutionKPIAnalyticsView', getattr(views, 'InstitutionKPIListView')).as_view(), name='institutionkpi_analytics'),
]

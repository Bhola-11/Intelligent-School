"""URL Routing for EduFlow Hostel Buildings, Blocks & Rooms (HostelFacilities)."""
from django.urls import path
try:
    from . import views_hostelfacilities as views
except ImportError:
    from . import views

app_name = 'hostel'

urlpatterns = [
    path('hostelfacilities/', getattr(views, 'HostelFacilitiesListView').as_view(), name='hostelfacilities_list'),
    path('hostelfacilities/create/', getattr(views, 'HostelFacilitiesCreateView').as_view(), name='hostelfacilities_create'),
    path('hostelfacilities/<int:pk>/', getattr(views, 'HostelFacilitiesDetailView').as_view(), name='hostelfacilities_detail'),
    path('hostelfacilities/<int:pk>/edit/', getattr(views, 'HostelFacilitiesUpdateView').as_view(), name='hostelfacilities_edit'),
    path('hostelfacilities/<int:pk>/delete/', getattr(views, 'HostelFacilitiesDeleteView').as_view(), name='hostelfacilities_delete'),
    path('hostelfacilities/<int:master_pk>/add-item/', getattr(views, 'HostelFacilitiesItemCreateView').as_view(), name='hostelfacilities_add_item'),
    path('hostelfacilities/<int:master_pk>/allocate/', getattr(views, 'HostelFacilitiesAllocationCreateView').as_view(), name='hostelfacilities_allocate'),
    path('hostelfacilities/bulk-update/', getattr(views, 'HostelFacilitiesBulkStatusUpdateView').as_view(), name='hostelfacilities_bulk_update'),
    path('hostelfacilities/export/csv/', getattr(views, 'HostelFacilitiesExportCSVView').as_view(), name='hostelfacilities_export_csv'),
    path('hostelfacilities/export/json/', getattr(views, 'HostelFacilitiesExportJSONView').as_view(), name='hostelfacilities_export_json'),
    path('hostelfacilities/api/list/', getattr(views, 'HostelFacilitiesAPIListView').as_view(), name='hostelfacilities_api_list'),
    path('hostelfacilities/<int:pk>/api/metrics/', getattr(views, 'HostelFacilitiesAPIMetricsView').as_view(), name='hostelfacilities_api_metrics'),
    path('hostelfacilities/dashboard/', getattr(views, 'HostelFacilitiesDashboardView', getattr(views, 'HostelFacilitiesListView')).as_view(), name='hostelfacilities_dashboard'),
    path('hostelfacilities/analytics/', getattr(views, 'HostelFacilitiesAnalyticsView', getattr(views, 'HostelFacilitiesListView')).as_view(), name='hostelfacilities_analytics'),
]

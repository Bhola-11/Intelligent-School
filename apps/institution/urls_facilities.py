"""URL Routing for EduFlow Buildings, Floors, Rooms & Facilities (Facilities)."""
from django.urls import path
try:
    from . import views_facilities as views
except ImportError:
    from . import views

app_name = 'institution'

urlpatterns = [
    path('facilities/', getattr(views, 'FacilitiesListView').as_view(), name='facilities_list'),
    path('facilities/create/', getattr(views, 'FacilitiesCreateView').as_view(), name='facilities_create'),
    path('facilities/<int:pk>/', getattr(views, 'FacilitiesDetailView').as_view(), name='facilities_detail'),
    path('facilities/<int:pk>/edit/', getattr(views, 'FacilitiesUpdateView').as_view(), name='facilities_edit'),
    path('facilities/<int:pk>/delete/', getattr(views, 'FacilitiesDeleteView').as_view(), name='facilities_delete'),
    path('facilities/<int:master_pk>/add-item/', getattr(views, 'FacilitiesItemCreateView').as_view(), name='facilities_add_item'),
    path('facilities/<int:master_pk>/allocate/', getattr(views, 'FacilitiesAllocationCreateView').as_view(), name='facilities_allocate'),
    path('facilities/bulk-update/', getattr(views, 'FacilitiesBulkStatusUpdateView').as_view(), name='facilities_bulk_update'),
    path('facilities/export/csv/', getattr(views, 'FacilitiesExportCSVView').as_view(), name='facilities_export_csv'),
    path('facilities/export/json/', getattr(views, 'FacilitiesExportJSONView').as_view(), name='facilities_export_json'),
    path('facilities/api/list/', getattr(views, 'FacilitiesAPIListView').as_view(), name='facilities_api_list'),
    path('facilities/<int:pk>/api/metrics/', getattr(views, 'FacilitiesAPIMetricsView').as_view(), name='facilities_api_metrics'),
    path('facilities/dashboard/', getattr(views, 'FacilitiesDashboardView', getattr(views, 'FacilitiesListView')).as_view(), name='facilities_dashboard'),
    path('facilities/analytics/', getattr(views, 'FacilitiesAnalyticsView', getattr(views, 'FacilitiesListView')).as_view(), name='facilities_analytics'),
]

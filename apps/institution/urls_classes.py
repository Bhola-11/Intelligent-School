"""URL Routing for EduFlow Class Levels, Sections & Batches (Classes)."""
from django.urls import path
try:
    from . import views_classes as views
except ImportError:
    from . import views

app_name = 'institution'

urlpatterns = [
    path('classes/', getattr(views, 'ClassesListView').as_view(), name='classes_list'),
    path('classes/create/', getattr(views, 'ClassesCreateView').as_view(), name='classes_create'),
    path('classes/<int:pk>/', getattr(views, 'ClassesDetailView').as_view(), name='classes_detail'),
    path('classes/<int:pk>/edit/', getattr(views, 'ClassesUpdateView').as_view(), name='classes_edit'),
    path('classes/<int:pk>/delete/', getattr(views, 'ClassesDeleteView').as_view(), name='classes_delete'),
    path('classes/<int:master_pk>/add-item/', getattr(views, 'ClassesItemCreateView').as_view(), name='classes_add_item'),
    path('classes/<int:master_pk>/allocate/', getattr(views, 'ClassesAllocationCreateView').as_view(), name='classes_allocate'),
    path('classes/bulk-update/', getattr(views, 'ClassesBulkStatusUpdateView').as_view(), name='classes_bulk_update'),
    path('classes/export/csv/', getattr(views, 'ClassesExportCSVView').as_view(), name='classes_export_csv'),
    path('classes/export/json/', getattr(views, 'ClassesExportJSONView').as_view(), name='classes_export_json'),
    path('classes/api/list/', getattr(views, 'ClassesAPIListView').as_view(), name='classes_api_list'),
    path('classes/<int:pk>/api/metrics/', getattr(views, 'ClassesAPIMetricsView').as_view(), name='classes_api_metrics'),
    path('classes/dashboard/', getattr(views, 'ClassesDashboardView', getattr(views, 'ClassesListView')).as_view(), name='classes_dashboard'),
    path('classes/analytics/', getattr(views, 'ClassesAnalyticsView', getattr(views, 'ClassesListView')).as_view(), name='classes_analytics'),
]

"""URL Routing for EduFlow Project Scaffolding & Core Architecture (Architecture)."""
from django.urls import path
try:
    from . import views_architecture as views
except ImportError:
    from . import views

app_name = 'core'

urlpatterns = [
    path('architecture/', getattr(views, 'ArchitectureListView').as_view(), name='architecture_list'),
    path('architecture/create/', getattr(views, 'ArchitectureCreateView').as_view(), name='architecture_create'),
    path('architecture/<int:pk>/', getattr(views, 'ArchitectureDetailView').as_view(), name='architecture_detail'),
    path('architecture/<int:pk>/edit/', getattr(views, 'ArchitectureUpdateView').as_view(), name='architecture_edit'),
    path('architecture/<int:pk>/delete/', getattr(views, 'ArchitectureDeleteView').as_view(), name='architecture_delete'),
    path('architecture/<int:master_pk>/add-item/', getattr(views, 'ArchitectureItemCreateView').as_view(), name='architecture_add_item'),
    path('architecture/<int:master_pk>/allocate/', getattr(views, 'ArchitectureAllocationCreateView').as_view(), name='architecture_allocate'),
    path('architecture/bulk-update/', getattr(views, 'ArchitectureBulkStatusUpdateView').as_view(), name='architecture_bulk_update'),
    path('architecture/export/csv/', getattr(views, 'ArchitectureExportCSVView').as_view(), name='architecture_export_csv'),
    path('architecture/export/json/', getattr(views, 'ArchitectureExportJSONView').as_view(), name='architecture_export_json'),
    path('architecture/api/list/', getattr(views, 'ArchitectureAPIListView').as_view(), name='architecture_api_list'),
    path('architecture/<int:pk>/api/metrics/', getattr(views, 'ArchitectureAPIMetricsView').as_view(), name='architecture_api_metrics'),
    path('architecture/dashboard/', getattr(views, 'ArchitectureDashboardView', getattr(views, 'ArchitectureListView')).as_view(), name='architecture_dashboard'),
    path('architecture/analytics/', getattr(views, 'ArchitectureAnalyticsView', getattr(views, 'ArchitectureListView')).as_view(), name='architecture_analytics'),
]

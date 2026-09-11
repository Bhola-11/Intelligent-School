"""URL Routing for EduFlow Library Circulation, Borrow & Returns (Circulation)."""
from django.urls import path
try:
    from . import views_circulation as views
except ImportError:
    from . import views

app_name = 'library'

urlpatterns = [
    path('circulation/', getattr(views, 'CirculationListView').as_view(), name='circulation_list'),
    path('circulation/create/', getattr(views, 'CirculationCreateView').as_view(), name='circulation_create'),
    path('circulation/<int:pk>/', getattr(views, 'CirculationDetailView').as_view(), name='circulation_detail'),
    path('circulation/<int:pk>/edit/', getattr(views, 'CirculationUpdateView').as_view(), name='circulation_edit'),
    path('circulation/<int:pk>/delete/', getattr(views, 'CirculationDeleteView').as_view(), name='circulation_delete'),
    path('circulation/<int:master_pk>/add-item/', getattr(views, 'CirculationItemCreateView').as_view(), name='circulation_add_item'),
    path('circulation/<int:master_pk>/allocate/', getattr(views, 'CirculationAllocationCreateView').as_view(), name='circulation_allocate'),
    path('circulation/bulk-update/', getattr(views, 'CirculationBulkStatusUpdateView').as_view(), name='circulation_bulk_update'),
    path('circulation/export/csv/', getattr(views, 'CirculationExportCSVView').as_view(), name='circulation_export_csv'),
    path('circulation/export/json/', getattr(views, 'CirculationExportJSONView').as_view(), name='circulation_export_json'),
    path('circulation/api/list/', getattr(views, 'CirculationAPIListView').as_view(), name='circulation_api_list'),
    path('circulation/<int:pk>/api/metrics/', getattr(views, 'CirculationAPIMetricsView').as_view(), name='circulation_api_metrics'),
    path('circulation/dashboard/', getattr(views, 'CirculationDashboardView', getattr(views, 'CirculationListView')).as_view(), name='circulation_dashboard'),
    path('circulation/analytics/', getattr(views, 'CirculationAnalyticsView', getattr(views, 'CirculationListView')).as_view(), name='circulation_analytics'),
]

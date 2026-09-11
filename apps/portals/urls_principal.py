"""URL Routing for EduFlow Principal & Director Portal (Principal)."""
from django.urls import path
try:
    from . import views_principal as views
except ImportError:
    from . import views

app_name = 'portals'

urlpatterns = [
    path('principal/', getattr(views, 'PrincipalListView').as_view(), name='principal_list'),
    path('principal/create/', getattr(views, 'PrincipalCreateView').as_view(), name='principal_create'),
    path('principal/<int:pk>/', getattr(views, 'PrincipalDetailView').as_view(), name='principal_detail'),
    path('principal/<int:pk>/edit/', getattr(views, 'PrincipalUpdateView').as_view(), name='principal_edit'),
    path('principal/<int:pk>/delete/', getattr(views, 'PrincipalDeleteView').as_view(), name='principal_delete'),
    path('principal/<int:master_pk>/add-item/', getattr(views, 'PrincipalItemCreateView').as_view(), name='principal_add_item'),
    path('principal/<int:master_pk>/allocate/', getattr(views, 'PrincipalAllocationCreateView').as_view(), name='principal_allocate'),
    path('principal/bulk-update/', getattr(views, 'PrincipalBulkStatusUpdateView').as_view(), name='principal_bulk_update'),
    path('principal/export/csv/', getattr(views, 'PrincipalExportCSVView').as_view(), name='principal_export_csv'),
    path('principal/export/json/', getattr(views, 'PrincipalExportJSONView').as_view(), name='principal_export_json'),
    path('principal/api/list/', getattr(views, 'PrincipalAPIListView').as_view(), name='principal_api_list'),
    path('principal/<int:pk>/api/metrics/', getattr(views, 'PrincipalAPIMetricsView').as_view(), name='principal_api_metrics'),
    path('principal/dashboard/', getattr(views, 'PrincipalDashboardView', getattr(views, 'PrincipalListView')).as_view(), name='principal_dashboard'),
    path('principal/analytics/', getattr(views, 'PrincipalAnalyticsView', getattr(views, 'PrincipalListView')).as_view(), name='principal_analytics'),
]

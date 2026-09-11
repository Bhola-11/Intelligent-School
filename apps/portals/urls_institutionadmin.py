"""URL Routing for EduFlow Institution Administrator Portal (InstitutionAdmin)."""
from django.urls import path
try:
    from . import views_institutionadmin as views
except ImportError:
    from . import views

app_name = 'portals'

urlpatterns = [
    path('institutionadmin/', getattr(views, 'InstitutionAdminListView').as_view(), name='institutionadmin_list'),
    path('institutionadmin/create/', getattr(views, 'InstitutionAdminCreateView').as_view(), name='institutionadmin_create'),
    path('institutionadmin/<int:pk>/', getattr(views, 'InstitutionAdminDetailView').as_view(), name='institutionadmin_detail'),
    path('institutionadmin/<int:pk>/edit/', getattr(views, 'InstitutionAdminUpdateView').as_view(), name='institutionadmin_edit'),
    path('institutionadmin/<int:pk>/delete/', getattr(views, 'InstitutionAdminDeleteView').as_view(), name='institutionadmin_delete'),
    path('institutionadmin/<int:master_pk>/add-item/', getattr(views, 'InstitutionAdminItemCreateView').as_view(), name='institutionadmin_add_item'),
    path('institutionadmin/<int:master_pk>/allocate/', getattr(views, 'InstitutionAdminAllocationCreateView').as_view(), name='institutionadmin_allocate'),
    path('institutionadmin/bulk-update/', getattr(views, 'InstitutionAdminBulkStatusUpdateView').as_view(), name='institutionadmin_bulk_update'),
    path('institutionadmin/export/csv/', getattr(views, 'InstitutionAdminExportCSVView').as_view(), name='institutionadmin_export_csv'),
    path('institutionadmin/export/json/', getattr(views, 'InstitutionAdminExportJSONView').as_view(), name='institutionadmin_export_json'),
    path('institutionadmin/api/list/', getattr(views, 'InstitutionAdminAPIListView').as_view(), name='institutionadmin_api_list'),
    path('institutionadmin/<int:pk>/api/metrics/', getattr(views, 'InstitutionAdminAPIMetricsView').as_view(), name='institutionadmin_api_metrics'),
    path('institutionadmin/dashboard/', getattr(views, 'InstitutionAdminDashboardView', getattr(views, 'InstitutionAdminListView')).as_view(), name='institutionadmin_dashboard'),
    path('institutionadmin/analytics/', getattr(views, 'InstitutionAdminAnalyticsView', getattr(views, 'InstitutionAdminListView')).as_view(), name='institutionadmin_analytics'),
]

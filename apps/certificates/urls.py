"""URL Routing for EduFlow Certificates Generation & QR Verification (Certificates)."""
from django.urls import path
try:
    from . import views_certificates as views
except ImportError:
    from . import views

app_name = 'certificates'

urlpatterns = [
    path('certificates/', getattr(views, 'CertificatesListView').as_view(), name='certificates_list'),
    path('certificates/create/', getattr(views, 'CertificatesCreateView').as_view(), name='certificates_create'),
    path('certificates/<int:pk>/', getattr(views, 'CertificatesDetailView').as_view(), name='certificates_detail'),
    path('certificates/<int:pk>/edit/', getattr(views, 'CertificatesUpdateView').as_view(), name='certificates_edit'),
    path('certificates/<int:pk>/delete/', getattr(views, 'CertificatesDeleteView').as_view(), name='certificates_delete'),
    path('certificates/<int:master_pk>/add-item/', getattr(views, 'CertificatesItemCreateView').as_view(), name='certificates_add_item'),
    path('certificates/<int:master_pk>/allocate/', getattr(views, 'CertificatesAllocationCreateView').as_view(), name='certificates_allocate'),
    path('certificates/bulk-update/', getattr(views, 'CertificatesBulkStatusUpdateView').as_view(), name='certificates_bulk_update'),
    path('certificates/export/csv/', getattr(views, 'CertificatesExportCSVView').as_view(), name='certificates_export_csv'),
    path('certificates/export/json/', getattr(views, 'CertificatesExportJSONView').as_view(), name='certificates_export_json'),
    path('certificates/api/list/', getattr(views, 'CertificatesAPIListView').as_view(), name='certificates_api_list'),
    path('certificates/<int:pk>/api/metrics/', getattr(views, 'CertificatesAPIMetricsView').as_view(), name='certificates_api_metrics'),
    path('certificates/dashboard/', getattr(views, 'CertificatesDashboardView', getattr(views, 'CertificatesListView')).as_view(), name='certificates_dashboard'),
    path('certificates/analytics/', getattr(views, 'CertificatesAnalyticsView', getattr(views, 'CertificatesListView')).as_view(), name='certificates_analytics'),
]

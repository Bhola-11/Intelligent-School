"""URL Routing for EduFlow Admission Offers & Student Account Provisioning (EnrollmentOffer)."""
from django.urls import path
try:
    from . import views_enrollmentoffer as views
except ImportError:
    from . import views

app_name = 'admissions'

urlpatterns = [
    path('enrollmentoffer/', getattr(views, 'EnrollmentOfferListView').as_view(), name='enrollmentoffer_list'),
    path('enrollmentoffer/create/', getattr(views, 'EnrollmentOfferCreateView').as_view(), name='enrollmentoffer_create'),
    path('enrollmentoffer/<int:pk>/', getattr(views, 'EnrollmentOfferDetailView').as_view(), name='enrollmentoffer_detail'),
    path('enrollmentoffer/<int:pk>/edit/', getattr(views, 'EnrollmentOfferUpdateView').as_view(), name='enrollmentoffer_edit'),
    path('enrollmentoffer/<int:pk>/delete/', getattr(views, 'EnrollmentOfferDeleteView').as_view(), name='enrollmentoffer_delete'),
    path('enrollmentoffer/<int:master_pk>/add-item/', getattr(views, 'EnrollmentOfferItemCreateView').as_view(), name='enrollmentoffer_add_item'),
    path('enrollmentoffer/<int:master_pk>/allocate/', getattr(views, 'EnrollmentOfferAllocationCreateView').as_view(), name='enrollmentoffer_allocate'),
    path('enrollmentoffer/bulk-update/', getattr(views, 'EnrollmentOfferBulkStatusUpdateView').as_view(), name='enrollmentoffer_bulk_update'),
    path('enrollmentoffer/export/csv/', getattr(views, 'EnrollmentOfferExportCSVView').as_view(), name='enrollmentoffer_export_csv'),
    path('enrollmentoffer/export/json/', getattr(views, 'EnrollmentOfferExportJSONView').as_view(), name='enrollmentoffer_export_json'),
    path('enrollmentoffer/api/list/', getattr(views, 'EnrollmentOfferAPIListView').as_view(), name='enrollmentoffer_api_list'),
    path('enrollmentoffer/<int:pk>/api/metrics/', getattr(views, 'EnrollmentOfferAPIMetricsView').as_view(), name='enrollmentoffer_api_metrics'),
    path('enrollmentoffer/dashboard/', getattr(views, 'EnrollmentOfferDashboardView', getattr(views, 'EnrollmentOfferListView')).as_view(), name='enrollmentoffer_dashboard'),
    path('enrollmentoffer/analytics/', getattr(views, 'EnrollmentOfferAnalyticsView', getattr(views, 'EnrollmentOfferListView')).as_view(), name='enrollmentoffer_analytics'),
]

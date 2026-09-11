"""URL Routing for EduFlow Admissions Document Verification Desk (Verification)."""
from django.urls import path
try:
    from . import views_verification as views
except ImportError:
    from . import views

app_name = 'admissions'

urlpatterns = [
    path('verification/', getattr(views, 'VerificationListView').as_view(), name='verification_list'),
    path('verification/create/', getattr(views, 'VerificationCreateView').as_view(), name='verification_create'),
    path('verification/<int:pk>/', getattr(views, 'VerificationDetailView').as_view(), name='verification_detail'),
    path('verification/<int:pk>/edit/', getattr(views, 'VerificationUpdateView').as_view(), name='verification_edit'),
    path('verification/<int:pk>/delete/', getattr(views, 'VerificationDeleteView').as_view(), name='verification_delete'),
    path('verification/<int:master_pk>/add-item/', getattr(views, 'VerificationItemCreateView').as_view(), name='verification_add_item'),
    path('verification/<int:master_pk>/allocate/', getattr(views, 'VerificationAllocationCreateView').as_view(), name='verification_allocate'),
    path('verification/bulk-update/', getattr(views, 'VerificationBulkStatusUpdateView').as_view(), name='verification_bulk_update'),
    path('verification/export/csv/', getattr(views, 'VerificationExportCSVView').as_view(), name='verification_export_csv'),
    path('verification/export/json/', getattr(views, 'VerificationExportJSONView').as_view(), name='verification_export_json'),
    path('verification/api/list/', getattr(views, 'VerificationAPIListView').as_view(), name='verification_api_list'),
    path('verification/<int:pk>/api/metrics/', getattr(views, 'VerificationAPIMetricsView').as_view(), name='verification_api_metrics'),
    path('verification/dashboard/', getattr(views, 'VerificationDashboardView', getattr(views, 'VerificationListView')).as_view(), name='verification_dashboard'),
    path('verification/analytics/', getattr(views, 'VerificationAnalyticsView', getattr(views, 'VerificationListView')).as_view(), name='verification_analytics'),
]

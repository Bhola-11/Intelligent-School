"""URL Routing for EduFlow Student Previous Education & Transfers (PreviousEducation)."""
from django.urls import path
try:
    from . import views_previouseducation as views
except ImportError:
    from . import views

app_name = 'students'

urlpatterns = [
    path('previouseducation/', getattr(views, 'PreviousEducationListView').as_view(), name='previouseducation_list'),
    path('previouseducation/create/', getattr(views, 'PreviousEducationCreateView').as_view(), name='previouseducation_create'),
    path('previouseducation/<int:pk>/', getattr(views, 'PreviousEducationDetailView').as_view(), name='previouseducation_detail'),
    path('previouseducation/<int:pk>/edit/', getattr(views, 'PreviousEducationUpdateView').as_view(), name='previouseducation_edit'),
    path('previouseducation/<int:pk>/delete/', getattr(views, 'PreviousEducationDeleteView').as_view(), name='previouseducation_delete'),
    path('previouseducation/<int:master_pk>/add-item/', getattr(views, 'PreviousEducationItemCreateView').as_view(), name='previouseducation_add_item'),
    path('previouseducation/<int:master_pk>/allocate/', getattr(views, 'PreviousEducationAllocationCreateView').as_view(), name='previouseducation_allocate'),
    path('previouseducation/bulk-update/', getattr(views, 'PreviousEducationBulkStatusUpdateView').as_view(), name='previouseducation_bulk_update'),
    path('previouseducation/export/csv/', getattr(views, 'PreviousEducationExportCSVView').as_view(), name='previouseducation_export_csv'),
    path('previouseducation/export/json/', getattr(views, 'PreviousEducationExportJSONView').as_view(), name='previouseducation_export_json'),
    path('previouseducation/api/list/', getattr(views, 'PreviousEducationAPIListView').as_view(), name='previouseducation_api_list'),
    path('previouseducation/<int:pk>/api/metrics/', getattr(views, 'PreviousEducationAPIMetricsView').as_view(), name='previouseducation_api_metrics'),
    path('previouseducation/dashboard/', getattr(views, 'PreviousEducationDashboardView', getattr(views, 'PreviousEducationListView')).as_view(), name='previouseducation_dashboard'),
    path('previouseducation/analytics/', getattr(views, 'PreviousEducationAnalyticsView', getattr(views, 'PreviousEducationListView')).as_view(), name='previouseducation_analytics'),
]

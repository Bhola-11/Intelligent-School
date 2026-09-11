"""URL Routing for EduFlow Disciplinary Hearings, Sanctions & Appeals (HearingsActions)."""
from django.urls import path
try:
    from . import views_hearingsactions as views
except ImportError:
    from . import views

app_name = 'discipline'

urlpatterns = [
    path('hearingsactions/', getattr(views, 'HearingsActionsListView').as_view(), name='hearingsactions_list'),
    path('hearingsactions/create/', getattr(views, 'HearingsActionsCreateView').as_view(), name='hearingsactions_create'),
    path('hearingsactions/<int:pk>/', getattr(views, 'HearingsActionsDetailView').as_view(), name='hearingsactions_detail'),
    path('hearingsactions/<int:pk>/edit/', getattr(views, 'HearingsActionsUpdateView').as_view(), name='hearingsactions_edit'),
    path('hearingsactions/<int:pk>/delete/', getattr(views, 'HearingsActionsDeleteView').as_view(), name='hearingsactions_delete'),
    path('hearingsactions/<int:master_pk>/add-item/', getattr(views, 'HearingsActionsItemCreateView').as_view(), name='hearingsactions_add_item'),
    path('hearingsactions/<int:master_pk>/allocate/', getattr(views, 'HearingsActionsAllocationCreateView').as_view(), name='hearingsactions_allocate'),
    path('hearingsactions/bulk-update/', getattr(views, 'HearingsActionsBulkStatusUpdateView').as_view(), name='hearingsactions_bulk_update'),
    path('hearingsactions/export/csv/', getattr(views, 'HearingsActionsExportCSVView').as_view(), name='hearingsactions_export_csv'),
    path('hearingsactions/export/json/', getattr(views, 'HearingsActionsExportJSONView').as_view(), name='hearingsactions_export_json'),
    path('hearingsactions/api/list/', getattr(views, 'HearingsActionsAPIListView').as_view(), name='hearingsactions_api_list'),
    path('hearingsactions/<int:pk>/api/metrics/', getattr(views, 'HearingsActionsAPIMetricsView').as_view(), name='hearingsactions_api_metrics'),
    path('hearingsactions/dashboard/', getattr(views, 'HearingsActionsDashboardView', getattr(views, 'HearingsActionsListView')).as_view(), name='hearingsactions_dashboard'),
    path('hearingsactions/analytics/', getattr(views, 'HearingsActionsAnalyticsView', getattr(views, 'HearingsActionsListView')).as_view(), name='hearingsactions_analytics'),
]

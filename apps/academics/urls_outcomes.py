"""URL Routing for EduFlow Learning Outcomes & Bloom's Taxonomy (Outcomes)."""
from django.urls import path
try:
    from . import views_outcomes as views
except ImportError:
    from . import views

app_name = 'academics'

urlpatterns = [
    path('outcomes/', getattr(views, 'OutcomesListView').as_view(), name='outcomes_list'),
    path('outcomes/create/', getattr(views, 'OutcomesCreateView').as_view(), name='outcomes_create'),
    path('outcomes/<int:pk>/', getattr(views, 'OutcomesDetailView').as_view(), name='outcomes_detail'),
    path('outcomes/<int:pk>/edit/', getattr(views, 'OutcomesUpdateView').as_view(), name='outcomes_edit'),
    path('outcomes/<int:pk>/delete/', getattr(views, 'OutcomesDeleteView').as_view(), name='outcomes_delete'),
    path('outcomes/<int:master_pk>/add-item/', getattr(views, 'OutcomesItemCreateView').as_view(), name='outcomes_add_item'),
    path('outcomes/<int:master_pk>/allocate/', getattr(views, 'OutcomesAllocationCreateView').as_view(), name='outcomes_allocate'),
    path('outcomes/bulk-update/', getattr(views, 'OutcomesBulkStatusUpdateView').as_view(), name='outcomes_bulk_update'),
    path('outcomes/export/csv/', getattr(views, 'OutcomesExportCSVView').as_view(), name='outcomes_export_csv'),
    path('outcomes/export/json/', getattr(views, 'OutcomesExportJSONView').as_view(), name='outcomes_export_json'),
    path('outcomes/api/list/', getattr(views, 'OutcomesAPIListView').as_view(), name='outcomes_api_list'),
    path('outcomes/<int:pk>/api/metrics/', getattr(views, 'OutcomesAPIMetricsView').as_view(), name='outcomes_api_metrics'),
    path('outcomes/dashboard/', getattr(views, 'OutcomesDashboardView', getattr(views, 'OutcomesListView')).as_view(), name='outcomes_dashboard'),
    path('outcomes/analytics/', getattr(views, 'OutcomesAnalyticsView', getattr(views, 'OutcomesListView')).as_view(), name='outcomes_analytics'),
]

"""URL Routing for EduFlow Event Participants & Competitions Tracker (Competitions)."""
from django.urls import path
try:
    from . import views_competitions as views
except ImportError:
    from . import views

app_name = 'events'

urlpatterns = [
    path('competitions/', getattr(views, 'CompetitionsListView').as_view(), name='competitions_list'),
    path('competitions/create/', getattr(views, 'CompetitionsCreateView').as_view(), name='competitions_create'),
    path('competitions/<int:pk>/', getattr(views, 'CompetitionsDetailView').as_view(), name='competitions_detail'),
    path('competitions/<int:pk>/edit/', getattr(views, 'CompetitionsUpdateView').as_view(), name='competitions_edit'),
    path('competitions/<int:pk>/delete/', getattr(views, 'CompetitionsDeleteView').as_view(), name='competitions_delete'),
    path('competitions/<int:master_pk>/add-item/', getattr(views, 'CompetitionsItemCreateView').as_view(), name='competitions_add_item'),
    path('competitions/<int:master_pk>/allocate/', getattr(views, 'CompetitionsAllocationCreateView').as_view(), name='competitions_allocate'),
    path('competitions/bulk-update/', getattr(views, 'CompetitionsBulkStatusUpdateView').as_view(), name='competitions_bulk_update'),
    path('competitions/export/csv/', getattr(views, 'CompetitionsExportCSVView').as_view(), name='competitions_export_csv'),
    path('competitions/export/json/', getattr(views, 'CompetitionsExportJSONView').as_view(), name='competitions_export_json'),
    path('competitions/api/list/', getattr(views, 'CompetitionsAPIListView').as_view(), name='competitions_api_list'),
    path('competitions/<int:pk>/api/metrics/', getattr(views, 'CompetitionsAPIMetricsView').as_view(), name='competitions_api_metrics'),
    path('competitions/dashboard/', getattr(views, 'CompetitionsDashboardView', getattr(views, 'CompetitionsListView')).as_view(), name='competitions_dashboard'),
    path('competitions/analytics/', getattr(views, 'CompetitionsAnalyticsView', getattr(views, 'CompetitionsListView')).as_view(), name='competitions_analytics'),
]

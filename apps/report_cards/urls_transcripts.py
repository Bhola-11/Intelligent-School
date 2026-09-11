"""URL Routing for EduFlow Multi-Year Transcripts & Academic Records (Transcripts)."""
from django.urls import path
try:
    from . import views_transcripts as views
except ImportError:
    from . import views

app_name = 'report_cards'

urlpatterns = [
    path('transcripts/', getattr(views, 'TranscriptsListView').as_view(), name='transcripts_list'),
    path('transcripts/create/', getattr(views, 'TranscriptsCreateView').as_view(), name='transcripts_create'),
    path('transcripts/<int:pk>/', getattr(views, 'TranscriptsDetailView').as_view(), name='transcripts_detail'),
    path('transcripts/<int:pk>/edit/', getattr(views, 'TranscriptsUpdateView').as_view(), name='transcripts_edit'),
    path('transcripts/<int:pk>/delete/', getattr(views, 'TranscriptsDeleteView').as_view(), name='transcripts_delete'),
    path('transcripts/<int:master_pk>/add-item/', getattr(views, 'TranscriptsItemCreateView').as_view(), name='transcripts_add_item'),
    path('transcripts/<int:master_pk>/allocate/', getattr(views, 'TranscriptsAllocationCreateView').as_view(), name='transcripts_allocate'),
    path('transcripts/bulk-update/', getattr(views, 'TranscriptsBulkStatusUpdateView').as_view(), name='transcripts_bulk_update'),
    path('transcripts/export/csv/', getattr(views, 'TranscriptsExportCSVView').as_view(), name='transcripts_export_csv'),
    path('transcripts/export/json/', getattr(views, 'TranscriptsExportJSONView').as_view(), name='transcripts_export_json'),
    path('transcripts/api/list/', getattr(views, 'TranscriptsAPIListView').as_view(), name='transcripts_api_list'),
    path('transcripts/<int:pk>/api/metrics/', getattr(views, 'TranscriptsAPIMetricsView').as_view(), name='transcripts_api_metrics'),
    path('transcripts/dashboard/', getattr(views, 'TranscriptsDashboardView', getattr(views, 'TranscriptsListView')).as_view(), name='transcripts_dashboard'),
    path('transcripts/analytics/', getattr(views, 'TranscriptsAnalyticsView', getattr(views, 'TranscriptsListView')).as_view(), name='transcripts_analytics'),
]

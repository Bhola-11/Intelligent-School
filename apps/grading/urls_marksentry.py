"""URL Routing for EduFlow Subject Marks & Component Entry Register (MarksEntry)."""
from django.urls import path
try:
    from . import views_marksentry as views
except ImportError:
    from . import views

app_name = 'grading'

urlpatterns = [
    path('marksentry/', getattr(views, 'MarksEntryListView').as_view(), name='marksentry_list'),
    path('marksentry/create/', getattr(views, 'MarksEntryCreateView').as_view(), name='marksentry_create'),
    path('marksentry/<int:pk>/', getattr(views, 'MarksEntryDetailView').as_view(), name='marksentry_detail'),
    path('marksentry/<int:pk>/edit/', getattr(views, 'MarksEntryUpdateView').as_view(), name='marksentry_edit'),
    path('marksentry/<int:pk>/delete/', getattr(views, 'MarksEntryDeleteView').as_view(), name='marksentry_delete'),
    path('marksentry/<int:master_pk>/add-item/', getattr(views, 'MarksEntryItemCreateView').as_view(), name='marksentry_add_item'),
    path('marksentry/<int:master_pk>/allocate/', getattr(views, 'MarksEntryAllocationCreateView').as_view(), name='marksentry_allocate'),
    path('marksentry/bulk-update/', getattr(views, 'MarksEntryBulkStatusUpdateView').as_view(), name='marksentry_bulk_update'),
    path('marksentry/export/csv/', getattr(views, 'MarksEntryExportCSVView').as_view(), name='marksentry_export_csv'),
    path('marksentry/export/json/', getattr(views, 'MarksEntryExportJSONView').as_view(), name='marksentry_export_json'),
    path('marksentry/api/list/', getattr(views, 'MarksEntryAPIListView').as_view(), name='marksentry_api_list'),
    path('marksentry/<int:pk>/api/metrics/', getattr(views, 'MarksEntryAPIMetricsView').as_view(), name='marksentry_api_metrics'),
    path('marksentry/dashboard/', getattr(views, 'MarksEntryDashboardView', getattr(views, 'MarksEntryListView')).as_view(), name='marksentry_dashboard'),
    path('marksentry/analytics/', getattr(views, 'MarksEntryAnalyticsView', getattr(views, 'MarksEntryListView')).as_view(), name='marksentry_analytics'),
]

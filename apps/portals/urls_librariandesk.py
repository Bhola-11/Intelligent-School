"""URL Routing for EduFlow Librarian Operations Center (LibrarianDesk)."""
from django.urls import path
try:
    from . import views_librariandesk as views
except ImportError:
    from . import views

app_name = 'portals'

urlpatterns = [
    path('librariandesk/', getattr(views, 'LibrarianDeskListView').as_view(), name='librariandesk_list'),
    path('librariandesk/create/', getattr(views, 'LibrarianDeskCreateView').as_view(), name='librariandesk_create'),
    path('librariandesk/<int:pk>/', getattr(views, 'LibrarianDeskDetailView').as_view(), name='librariandesk_detail'),
    path('librariandesk/<int:pk>/edit/', getattr(views, 'LibrarianDeskUpdateView').as_view(), name='librariandesk_edit'),
    path('librariandesk/<int:pk>/delete/', getattr(views, 'LibrarianDeskDeleteView').as_view(), name='librariandesk_delete'),
    path('librariandesk/<int:master_pk>/add-item/', getattr(views, 'LibrarianDeskItemCreateView').as_view(), name='librariandesk_add_item'),
    path('librariandesk/<int:master_pk>/allocate/', getattr(views, 'LibrarianDeskAllocationCreateView').as_view(), name='librariandesk_allocate'),
    path('librariandesk/bulk-update/', getattr(views, 'LibrarianDeskBulkStatusUpdateView').as_view(), name='librariandesk_bulk_update'),
    path('librariandesk/export/csv/', getattr(views, 'LibrarianDeskExportCSVView').as_view(), name='librariandesk_export_csv'),
    path('librariandesk/export/json/', getattr(views, 'LibrarianDeskExportJSONView').as_view(), name='librariandesk_export_json'),
    path('librariandesk/api/list/', getattr(views, 'LibrarianDeskAPIListView').as_view(), name='librariandesk_api_list'),
    path('librariandesk/<int:pk>/api/metrics/', getattr(views, 'LibrarianDeskAPIMetricsView').as_view(), name='librariandesk_api_metrics'),
    path('librariandesk/dashboard/', getattr(views, 'LibrarianDeskDashboardView', getattr(views, 'LibrarianDeskListView')).as_view(), name='librariandesk_dashboard'),
    path('librariandesk/analytics/', getattr(views, 'LibrarianDeskAnalyticsView', getattr(views, 'LibrarianDeskListView')).as_view(), name='librariandesk_analytics'),
]

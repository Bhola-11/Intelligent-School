"""URL Routing for EduFlow Notice Board & Announcements (NoticeBoard)."""
from django.urls import path
try:
    from . import views_noticeboard as views
except ImportError:
    from . import views

app_name = 'communication'

urlpatterns = [
    path('noticeboard/', getattr(views, 'NoticeBoardListView').as_view(), name='noticeboard_list'),
    path('noticeboard/create/', getattr(views, 'NoticeBoardCreateView').as_view(), name='noticeboard_create'),
    path('noticeboard/<int:pk>/', getattr(views, 'NoticeBoardDetailView').as_view(), name='noticeboard_detail'),
    path('noticeboard/<int:pk>/edit/', getattr(views, 'NoticeBoardUpdateView').as_view(), name='noticeboard_edit'),
    path('noticeboard/<int:pk>/delete/', getattr(views, 'NoticeBoardDeleteView').as_view(), name='noticeboard_delete'),
    path('noticeboard/<int:master_pk>/add-item/', getattr(views, 'NoticeBoardItemCreateView').as_view(), name='noticeboard_add_item'),
    path('noticeboard/<int:master_pk>/allocate/', getattr(views, 'NoticeBoardAllocationCreateView').as_view(), name='noticeboard_allocate'),
    path('noticeboard/bulk-update/', getattr(views, 'NoticeBoardBulkStatusUpdateView').as_view(), name='noticeboard_bulk_update'),
    path('noticeboard/export/csv/', getattr(views, 'NoticeBoardExportCSVView').as_view(), name='noticeboard_export_csv'),
    path('noticeboard/export/json/', getattr(views, 'NoticeBoardExportJSONView').as_view(), name='noticeboard_export_json'),
    path('noticeboard/api/list/', getattr(views, 'NoticeBoardAPIListView').as_view(), name='noticeboard_api_list'),
    path('noticeboard/<int:pk>/api/metrics/', getattr(views, 'NoticeBoardAPIMetricsView').as_view(), name='noticeboard_api_metrics'),
    path('noticeboard/dashboard/', getattr(views, 'NoticeBoardDashboardView', getattr(views, 'NoticeBoardListView')).as_view(), name='noticeboard_dashboard'),
    path('noticeboard/analytics/', getattr(views, 'NoticeBoardAnalyticsView', getattr(views, 'NoticeBoardListView')).as_view(), name='noticeboard_analytics'),
]

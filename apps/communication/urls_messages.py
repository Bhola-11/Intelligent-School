"""URL Routing for EduFlow Internal Messaging & Communication Threads (Messages)."""
from django.urls import path
try:
    from . import views_messages as views
except ImportError:
    from . import views

app_name = 'communication'

urlpatterns = [
    path('messages/', getattr(views, 'MessagesListView').as_view(), name='messages_list'),
    path('messages/create/', getattr(views, 'MessagesCreateView').as_view(), name='messages_create'),
    path('messages/<int:pk>/', getattr(views, 'MessagesDetailView').as_view(), name='messages_detail'),
    path('messages/<int:pk>/edit/', getattr(views, 'MessagesUpdateView').as_view(), name='messages_edit'),
    path('messages/<int:pk>/delete/', getattr(views, 'MessagesDeleteView').as_view(), name='messages_delete'),
    path('messages/<int:master_pk>/add-item/', getattr(views, 'MessagesItemCreateView').as_view(), name='messages_add_item'),
    path('messages/<int:master_pk>/allocate/', getattr(views, 'MessagesAllocationCreateView').as_view(), name='messages_allocate'),
    path('messages/bulk-update/', getattr(views, 'MessagesBulkStatusUpdateView').as_view(), name='messages_bulk_update'),
    path('messages/export/csv/', getattr(views, 'MessagesExportCSVView').as_view(), name='messages_export_csv'),
    path('messages/export/json/', getattr(views, 'MessagesExportJSONView').as_view(), name='messages_export_json'),
    path('messages/api/list/', getattr(views, 'MessagesAPIListView').as_view(), name='messages_api_list'),
    path('messages/<int:pk>/api/metrics/', getattr(views, 'MessagesAPIMetricsView').as_view(), name='messages_api_metrics'),
    path('messages/dashboard/', getattr(views, 'MessagesDashboardView', getattr(views, 'MessagesListView')).as_view(), name='messages_dashboard'),
    path('messages/analytics/', getattr(views, 'MessagesAnalyticsView', getattr(views, 'MessagesListView')).as_view(), name='messages_analytics'),
]

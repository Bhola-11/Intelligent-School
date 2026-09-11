"""URL Routing for EduFlow Room Allocation & Facility Optimization (RoomAllocator)."""
from django.urls import path
try:
    from . import views_roomallocator as views
except ImportError:
    from . import views

app_name = 'timetable'

urlpatterns = [
    path('roomallocator/', getattr(views, 'RoomAllocatorListView').as_view(), name='roomallocator_list'),
    path('roomallocator/create/', getattr(views, 'RoomAllocatorCreateView').as_view(), name='roomallocator_create'),
    path('roomallocator/<int:pk>/', getattr(views, 'RoomAllocatorDetailView').as_view(), name='roomallocator_detail'),
    path('roomallocator/<int:pk>/edit/', getattr(views, 'RoomAllocatorUpdateView').as_view(), name='roomallocator_edit'),
    path('roomallocator/<int:pk>/delete/', getattr(views, 'RoomAllocatorDeleteView').as_view(), name='roomallocator_delete'),
    path('roomallocator/<int:master_pk>/add-item/', getattr(views, 'RoomAllocatorItemCreateView').as_view(), name='roomallocator_add_item'),
    path('roomallocator/<int:master_pk>/allocate/', getattr(views, 'RoomAllocatorAllocationCreateView').as_view(), name='roomallocator_allocate'),
    path('roomallocator/bulk-update/', getattr(views, 'RoomAllocatorBulkStatusUpdateView').as_view(), name='roomallocator_bulk_update'),
    path('roomallocator/export/csv/', getattr(views, 'RoomAllocatorExportCSVView').as_view(), name='roomallocator_export_csv'),
    path('roomallocator/export/json/', getattr(views, 'RoomAllocatorExportJSONView').as_view(), name='roomallocator_export_json'),
    path('roomallocator/api/list/', getattr(views, 'RoomAllocatorAPIListView').as_view(), name='roomallocator_api_list'),
    path('roomallocator/<int:pk>/api/metrics/', getattr(views, 'RoomAllocatorAPIMetricsView').as_view(), name='roomallocator_api_metrics'),
    path('roomallocator/dashboard/', getattr(views, 'RoomAllocatorDashboardView', getattr(views, 'RoomAllocatorListView')).as_view(), name='roomallocator_dashboard'),
    path('roomallocator/analytics/', getattr(views, 'RoomAllocatorAnalyticsView', getattr(views, 'RoomAllocatorListView')).as_view(), name='roomallocator_analytics'),
]

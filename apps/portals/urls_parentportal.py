"""URL Routing for EduFlow Parent & Guardian Multi-Child Portal (ParentPortal)."""
from django.urls import path
try:
    from . import views_parentportal as views
except ImportError:
    from . import views

app_name = 'portals'

urlpatterns = [
    path('parentportal/', getattr(views, 'ParentPortalListView').as_view(), name='parentportal_list'),
    path('parentportal/create/', getattr(views, 'ParentPortalCreateView').as_view(), name='parentportal_create'),
    path('parentportal/<int:pk>/', getattr(views, 'ParentPortalDetailView').as_view(), name='parentportal_detail'),
    path('parentportal/<int:pk>/edit/', getattr(views, 'ParentPortalUpdateView').as_view(), name='parentportal_edit'),
    path('parentportal/<int:pk>/delete/', getattr(views, 'ParentPortalDeleteView').as_view(), name='parentportal_delete'),
    path('parentportal/<int:master_pk>/add-item/', getattr(views, 'ParentPortalItemCreateView').as_view(), name='parentportal_add_item'),
    path('parentportal/<int:master_pk>/allocate/', getattr(views, 'ParentPortalAllocationCreateView').as_view(), name='parentportal_allocate'),
    path('parentportal/bulk-update/', getattr(views, 'ParentPortalBulkStatusUpdateView').as_view(), name='parentportal_bulk_update'),
    path('parentportal/export/csv/', getattr(views, 'ParentPortalExportCSVView').as_view(), name='parentportal_export_csv'),
    path('parentportal/export/json/', getattr(views, 'ParentPortalExportJSONView').as_view(), name='parentportal_export_json'),
    path('parentportal/api/list/', getattr(views, 'ParentPortalAPIListView').as_view(), name='parentportal_api_list'),
    path('parentportal/<int:pk>/api/metrics/', getattr(views, 'ParentPortalAPIMetricsView').as_view(), name='parentportal_api_metrics'),
    path('parentportal/dashboard/', getattr(views, 'ParentPortalDashboardView', getattr(views, 'ParentPortalListView')).as_view(), name='parentportal_dashboard'),
    path('parentportal/analytics/', getattr(views, 'ParentPortalAnalyticsView', getattr(views, 'ParentPortalListView')).as_view(), name='parentportal_analytics'),
]

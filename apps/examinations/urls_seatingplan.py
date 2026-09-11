"""URL Routing for EduFlow Exam Seating Arrangement & Desk Planner (SeatingPlan)."""
from django.urls import path
try:
    from . import views_seatingplan as views
except ImportError:
    from . import views

app_name = 'examinations'

urlpatterns = [
    path('seatingplan/', getattr(views, 'SeatingPlanListView').as_view(), name='seatingplan_list'),
    path('seatingplan/create/', getattr(views, 'SeatingPlanCreateView').as_view(), name='seatingplan_create'),
    path('seatingplan/<int:pk>/', getattr(views, 'SeatingPlanDetailView').as_view(), name='seatingplan_detail'),
    path('seatingplan/<int:pk>/edit/', getattr(views, 'SeatingPlanUpdateView').as_view(), name='seatingplan_edit'),
    path('seatingplan/<int:pk>/delete/', getattr(views, 'SeatingPlanDeleteView').as_view(), name='seatingplan_delete'),
    path('seatingplan/<int:master_pk>/add-item/', getattr(views, 'SeatingPlanItemCreateView').as_view(), name='seatingplan_add_item'),
    path('seatingplan/<int:master_pk>/allocate/', getattr(views, 'SeatingPlanAllocationCreateView').as_view(), name='seatingplan_allocate'),
    path('seatingplan/bulk-update/', getattr(views, 'SeatingPlanBulkStatusUpdateView').as_view(), name='seatingplan_bulk_update'),
    path('seatingplan/export/csv/', getattr(views, 'SeatingPlanExportCSVView').as_view(), name='seatingplan_export_csv'),
    path('seatingplan/export/json/', getattr(views, 'SeatingPlanExportJSONView').as_view(), name='seatingplan_export_json'),
    path('seatingplan/api/list/', getattr(views, 'SeatingPlanAPIListView').as_view(), name='seatingplan_api_list'),
    path('seatingplan/<int:pk>/api/metrics/', getattr(views, 'SeatingPlanAPIMetricsView').as_view(), name='seatingplan_api_metrics'),
    path('seatingplan/dashboard/', getattr(views, 'SeatingPlanDashboardView', getattr(views, 'SeatingPlanListView')).as_view(), name='seatingplan_dashboard'),
    path('seatingplan/analytics/', getattr(views, 'SeatingPlanAnalyticsView', getattr(views, 'SeatingPlanListView')).as_view(), name='seatingplan_analytics'),
]

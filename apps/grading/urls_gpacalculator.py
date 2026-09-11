"""URL Routing for EduFlow GPA, CGPA, Term Average & Rank Engine (GPACalculator)."""
from django.urls import path
try:
    from . import views_gpacalculator as views
except ImportError:
    from . import views

app_name = 'grading'

urlpatterns = [
    path('gpacalculator/', getattr(views, 'GPACalculatorListView').as_view(), name='gpacalculator_list'),
    path('gpacalculator/create/', getattr(views, 'GPACalculatorCreateView').as_view(), name='gpacalculator_create'),
    path('gpacalculator/<int:pk>/', getattr(views, 'GPACalculatorDetailView').as_view(), name='gpacalculator_detail'),
    path('gpacalculator/<int:pk>/edit/', getattr(views, 'GPACalculatorUpdateView').as_view(), name='gpacalculator_edit'),
    path('gpacalculator/<int:pk>/delete/', getattr(views, 'GPACalculatorDeleteView').as_view(), name='gpacalculator_delete'),
    path('gpacalculator/<int:master_pk>/add-item/', getattr(views, 'GPACalculatorItemCreateView').as_view(), name='gpacalculator_add_item'),
    path('gpacalculator/<int:master_pk>/allocate/', getattr(views, 'GPACalculatorAllocationCreateView').as_view(), name='gpacalculator_allocate'),
    path('gpacalculator/bulk-update/', getattr(views, 'GPACalculatorBulkStatusUpdateView').as_view(), name='gpacalculator_bulk_update'),
    path('gpacalculator/export/csv/', getattr(views, 'GPACalculatorExportCSVView').as_view(), name='gpacalculator_export_csv'),
    path('gpacalculator/export/json/', getattr(views, 'GPACalculatorExportJSONView').as_view(), name='gpacalculator_export_json'),
    path('gpacalculator/api/list/', getattr(views, 'GPACalculatorAPIListView').as_view(), name='gpacalculator_api_list'),
    path('gpacalculator/<int:pk>/api/metrics/', getattr(views, 'GPACalculatorAPIMetricsView').as_view(), name='gpacalculator_api_metrics'),
    path('gpacalculator/dashboard/', getattr(views, 'GPACalculatorDashboardView', getattr(views, 'GPACalculatorListView')).as_view(), name='gpacalculator_dashboard'),
    path('gpacalculator/analytics/', getattr(views, 'GPACalculatorAnalyticsView', getattr(views, 'GPACalculatorListView')).as_view(), name='gpacalculator_analytics'),
]

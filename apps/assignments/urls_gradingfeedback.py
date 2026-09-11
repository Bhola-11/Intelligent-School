"""URL Routing for EduFlow Assignment Grading, Rubrics & Feedback (GradingFeedback)."""
from django.urls import path
try:
    from . import views_gradingfeedback as views
except ImportError:
    from . import views

app_name = 'assignments'

urlpatterns = [
    path('gradingfeedback/', getattr(views, 'GradingFeedbackListView').as_view(), name='gradingfeedback_list'),
    path('gradingfeedback/create/', getattr(views, 'GradingFeedbackCreateView').as_view(), name='gradingfeedback_create'),
    path('gradingfeedback/<int:pk>/', getattr(views, 'GradingFeedbackDetailView').as_view(), name='gradingfeedback_detail'),
    path('gradingfeedback/<int:pk>/edit/', getattr(views, 'GradingFeedbackUpdateView').as_view(), name='gradingfeedback_edit'),
    path('gradingfeedback/<int:pk>/delete/', getattr(views, 'GradingFeedbackDeleteView').as_view(), name='gradingfeedback_delete'),
    path('gradingfeedback/<int:master_pk>/add-item/', getattr(views, 'GradingFeedbackItemCreateView').as_view(), name='gradingfeedback_add_item'),
    path('gradingfeedback/<int:master_pk>/allocate/', getattr(views, 'GradingFeedbackAllocationCreateView').as_view(), name='gradingfeedback_allocate'),
    path('gradingfeedback/bulk-update/', getattr(views, 'GradingFeedbackBulkStatusUpdateView').as_view(), name='gradingfeedback_bulk_update'),
    path('gradingfeedback/export/csv/', getattr(views, 'GradingFeedbackExportCSVView').as_view(), name='gradingfeedback_export_csv'),
    path('gradingfeedback/export/json/', getattr(views, 'GradingFeedbackExportJSONView').as_view(), name='gradingfeedback_export_json'),
    path('gradingfeedback/api/list/', getattr(views, 'GradingFeedbackAPIListView').as_view(), name='gradingfeedback_api_list'),
    path('gradingfeedback/<int:pk>/api/metrics/', getattr(views, 'GradingFeedbackAPIMetricsView').as_view(), name='gradingfeedback_api_metrics'),
    path('gradingfeedback/dashboard/', getattr(views, 'GradingFeedbackDashboardView', getattr(views, 'GradingFeedbackListView')).as_view(), name='gradingfeedback_dashboard'),
    path('gradingfeedback/analytics/', getattr(views, 'GradingFeedbackAnalyticsView', getattr(views, 'GradingFeedbackListView')).as_view(), name='gradingfeedback_analytics'),
]

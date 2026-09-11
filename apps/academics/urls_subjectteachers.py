"""URL Routing for EduFlow Teacher-Class-Subject Allocation Matrix (SubjectTeachers)."""
from django.urls import path
try:
    from . import views_subjectteachers as views
except ImportError:
    from . import views

app_name = 'academics'

urlpatterns = [
    path('subjectteachers/', getattr(views, 'SubjectTeachersListView').as_view(), name='subjectteachers_list'),
    path('subjectteachers/create/', getattr(views, 'SubjectTeachersCreateView').as_view(), name='subjectteachers_create'),
    path('subjectteachers/<int:pk>/', getattr(views, 'SubjectTeachersDetailView').as_view(), name='subjectteachers_detail'),
    path('subjectteachers/<int:pk>/edit/', getattr(views, 'SubjectTeachersUpdateView').as_view(), name='subjectteachers_edit'),
    path('subjectteachers/<int:pk>/delete/', getattr(views, 'SubjectTeachersDeleteView').as_view(), name='subjectteachers_delete'),
    path('subjectteachers/<int:master_pk>/add-item/', getattr(views, 'SubjectTeachersItemCreateView').as_view(), name='subjectteachers_add_item'),
    path('subjectteachers/<int:master_pk>/allocate/', getattr(views, 'SubjectTeachersAllocationCreateView').as_view(), name='subjectteachers_allocate'),
    path('subjectteachers/bulk-update/', getattr(views, 'SubjectTeachersBulkStatusUpdateView').as_view(), name='subjectteachers_bulk_update'),
    path('subjectteachers/export/csv/', getattr(views, 'SubjectTeachersExportCSVView').as_view(), name='subjectteachers_export_csv'),
    path('subjectteachers/export/json/', getattr(views, 'SubjectTeachersExportJSONView').as_view(), name='subjectteachers_export_json'),
    path('subjectteachers/api/list/', getattr(views, 'SubjectTeachersAPIListView').as_view(), name='subjectteachers_api_list'),
    path('subjectteachers/<int:pk>/api/metrics/', getattr(views, 'SubjectTeachersAPIMetricsView').as_view(), name='subjectteachers_api_metrics'),
    path('subjectteachers/dashboard/', getattr(views, 'SubjectTeachersDashboardView', getattr(views, 'SubjectTeachersListView')).as_view(), name='subjectteachers_dashboard'),
    path('subjectteachers/analytics/', getattr(views, 'SubjectTeachersAnalyticsView', getattr(views, 'SubjectTeachersListView')).as_view(), name='subjectteachers_analytics'),
]

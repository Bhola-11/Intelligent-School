"""
Main URL Configuration for EduFlow Enterprise Platform.
Routes all 33 modular applications and portal dashboards.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    
    # Application Route Registrations
    path('core/', include('apps.core.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('institution/', include('apps.institution.urls')),
    path('students/', include('apps.students.urls')),
    path('admissions/', include('apps.admissions.urls')),
    path('staff/', include('apps.staff.urls')),
    path('attendance/', include('apps.attendance.urls')),
    path('academics/', include('apps.academics.urls')),
    path('timetable/', include('apps.timetable.urls')),
    path('assignments/', include('apps.assignments.urls')),
    path('examinations/', include('apps.examinations.urls')),
    path('grading/', include('apps.grading.urls')),
    path('report-cards/', include('apps.report_cards.urls')),
    path('analytics/', include('apps.analytics.urls')),
    path('portals/', include('apps.portals.urls')),
    path('fees/', include('apps.fees.urls')),
    path('accounting/', include('apps.accounting.urls')),
    path('library/', include('apps.library.urls')),
    path('communication/', include('apps.communication.urls')),
    path('notifications/', include('apps.notifications.urls')),
    path('leaves/', include('apps.leaves.urls')),
    path('events/', include('apps.events.urls')),
    path('transport/', include('apps.transport.urls')),
    path('hostel/', include('apps.hostel.urls')),
    path('inventory/', include('apps.inventory.urls')),
    path('maintenance/', include('apps.maintenance.urls')),
    path('documents/', include('apps.documents.urls')),
    path('certificates/', include('apps.certificates.urls')),
    path('discipline/', include('apps.discipline.urls')),
    path('counseling/', include('apps.counseling.urls')),
    path('reports/', include('apps.reports.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

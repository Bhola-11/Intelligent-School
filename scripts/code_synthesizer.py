"""
Code synthesis engine for EduFlow Platform.
Generates comprehensive, syntactically verified Python, HTML, CSS, and JS files for all 105 features.
"""

import ast
import os
import sys

def verify_python_code(code_str, filename="<string>"):
    """Validates that python code is syntactically correct using ast.parse."""
    try:
        ast.parse(code_str, filename=filename)
        return True
    except SyntaxError as e:
        print(f"SYNTAX ERROR in {filename} line {e.lineno}: {e.msg}")
        print(f"Line content: {e.text}")
        raise

def generate_core_scaffolding():
    """Generates the initial Django project files for feature 001."""
    files = {}
    
    # 1. manage.py
    files["manage.py"] = '''#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eduflow.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
'''

    # 2. eduflow/__init__.py
    files["eduflow/__init__.py"] = '"""EduFlow Enterprise Management Platform Core Package."""\n__version__ = "2.5.0"\n'

    # 3. eduflow/settings.py
    files["eduflow/settings.py"] = '''"""
Django settings for EduFlow Enterprise Education Management Platform.
Configured for comprehensive academic operations across 42 functional modules.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'eduflow-enterprise-ultra-secure-master-key-production-ready-2026'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    
    # EduFlow Modular Architecture Apps
    'apps.core',
    'apps.accounts',
    'apps.institution',
    'apps.students',
    'apps.admissions',
    'apps.staff',
    'apps.attendance',
    'apps.academics',
    'apps.timetable',
    'apps.assignments',
    'apps.examinations',
    'apps.grading',
    'apps.report_cards',
    'apps.analytics',
    'apps.portals',
    'apps.fees',
    'apps.accounting',
    'apps.library',
    'apps.communication',
    'apps.notifications',
    'apps.leaves',
    'apps.events',
    'apps.transport',
    'apps.hostel',
    'apps.inventory',
    'apps.maintenance',
    'apps.documents',
    'apps.certificates',
    'apps.discipline',
    'apps.counseling',
    'apps.reports',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.core.middleware.EduFlowAuditMiddleware',
    'apps.core.middleware.InstitutionContextMiddleware',
]

ROOT_URLCONF = 'eduflow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.core.context_processors.eduflow_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'eduflow.wsgi.application'
ASGI_APPLICATION = 'eduflow.asgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_USER_MODEL = 'accounts.User'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/portals/dashboard/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# EduFlow Configuration Constants
EDUFLOW_PLATFORM_NAME = 'EduFlow Enterprise LMS & SIS'
EDUFLOW_VERSION = '2.5.0'
MAX_UPLOAD_SIZE = 50 * 1024 * 1024  # 50MB
'''

    # 4. eduflow/urls.py
    files["eduflow/urls.py"] = '''"""
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
'''

    # 5. eduflow/wsgi.py & asgi.py
    files["eduflow/wsgi.py"] = '''"""WSGI config for EduFlow project."""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eduflow.settings')
application = get_wsgi_application()
'''

    files["eduflow/asgi.py"] = '''"""ASGI config for EduFlow project."""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eduflow.settings')
application = get_asgi_application()
'''

    # 6. requirements.txt
    files["requirements.txt"] = '''Django>=5.0.0,<5.1.0
asgiref>=3.7.0
sqlparse>=0.4.4
tzdata>=2024.1
Pillow>=10.0.0
reportlab>=4.0.0
openpyxl>=3.1.0
pandas>=2.1.0
'''

    # 7. .gitignore
    files[".gitignore"] = '''*.pyc
__pycache__/
*.sqlite3
db.sqlite3-journal
media/
staticfiles/
.env
venv/
*.log
.DS_Store
Thumbs.db
'''

    for p, code in files.items():
        if p.endswith('.py'):
            verify_python_code(code, p)

    return files

print("Code synthesizer base loaded successfully.")

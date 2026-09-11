"""
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

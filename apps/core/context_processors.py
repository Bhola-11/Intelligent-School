"""EduFlow Global Context Processors."""
from django.conf import settings

def eduflow_context(request):
    """Injects platform branding, active session and user role info."""
    role = getattr(request.user, 'role', 'Guest') if request.user.is_authenticated else 'Guest'
    return {
        'PLATFORM_NAME': getattr(settings, 'EDUFLOW_PLATFORM_NAME', 'EduFlow'),
        'PLATFORM_VERSION': getattr(settings, 'EDUFLOW_VERSION', '2.5.0'),
        'USER_ROLE': role,
        'IS_SUPERADMIN': role == 'SuperAdmin',
        'IS_TEACHER': role == 'Teacher',
        'IS_STUDENT': role == 'Student',
        'IS_PARENT': role == 'Parent',
        'IS_ACCOUNTANT': role == 'Accountant',
    }

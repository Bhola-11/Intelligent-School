"""EduFlow Core Middleware for audit trails and institution tenancy."""
import time
import logging

logger = logging.getLogger(__name__)

class EduFlowAuditMiddleware:
    """Captures request-response cycle metadata for compliance auditing."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - request.start_time
        response['X-EduFlow-Execution-Time'] = f"{duration:.3f}s"
        return response

class InstitutionContextMiddleware:
    """Injects current active institution and academic session context."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            request.active_institution_id = getattr(request.user, 'institution_id', 1)
        else:
            request.active_institution_id = None
        return self.get_response(request)

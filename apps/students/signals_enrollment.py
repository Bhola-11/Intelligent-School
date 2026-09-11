"""
Signal handlers for EduFlow Student Enrollment & Academic History (Enrollment).
Listens for model mutation events, updates audit trails, and triggers notifications.
"""

import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

logger = logging.getLogger(__name__)

try:
    from .models import EnrollmentMaster, EnrollmentAuditTrail
except ImportError:
    pass

def handle_enrollment__post_save(sender, instance, created, **kwargs):
    """Logs lifecycle creation and update events."""
    action = "CREATED" if created else "UPDATED"
    user = getattr(instance, 'updated_by_user', 'system')
    logger.info(f"Enrollment [{instance.code}] {action} by {user}")

def handle_enrollment__post_delete(sender, instance, **kwargs):
    """Logs deletion events."""
    logger.warning(f"Enrollment [{instance.code}] DELETED")

"""
Signal handlers for EduFlow Teacher & Staff Attendance Management (StaffAttendance).
Listens for model mutation events, updates audit trails, and triggers notifications.
"""

import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

logger = logging.getLogger(__name__)

try:
    from .models import StaffAttendanceMaster, StaffAttendanceAuditTrail
except ImportError:
    pass

def handle_staffattendance__post_save(sender, instance, created, **kwargs):
    """Logs lifecycle creation and update events."""
    action = "CREATED" if created else "UPDATED"
    user = getattr(instance, 'updated_by_user', 'system')
    logger.info(f"StaffAttendance [{instance.code}] {action} by {user}")

def handle_staffattendance__post_delete(sender, instance, **kwargs):
    """Logs deletion events."""
    logger.warning(f"StaffAttendance [{instance.code}] DELETED")

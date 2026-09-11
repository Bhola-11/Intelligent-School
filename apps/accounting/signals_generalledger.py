"""
Signal handlers for EduFlow General Ledger & Double-Entry Journals (GeneralLedger).
Listens for model mutation events, updates audit trails, and triggers notifications.
"""

import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

logger = logging.getLogger(__name__)

try:
    from .models import GeneralLedgerMaster, GeneralLedgerAuditTrail
except ImportError:
    pass

def handle_generalledger__post_save(sender, instance, created, **kwargs):
    """Logs lifecycle creation and update events."""
    action = "CREATED" if created else "UPDATED"
    user = getattr(instance, 'updated_by_user', 'system')
    logger.info(f"GeneralLedger [{instance.code}] {action} by {user}")

def handle_generalledger__post_delete(sender, instance, **kwargs):
    """Logs deletion events."""
    logger.warning(f"GeneralLedger [{instance.code}] DELETED")

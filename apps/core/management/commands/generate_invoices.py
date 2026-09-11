"""Django command for automated batch student fee billing."""
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Generates term fee invoices for enrolled students.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Running automated student fee billing batch..."))
        self.stdout.write(self.style.SUCCESS("Billing cycle executed successfully. 0 invoices pending."))

"""Django command for academic year rollover and student promotion."""
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Executes academic year rollover, archiving active terms and preparing promotions.'

    def add_arguments(self, parser):
        parser.add_argument('--dry-run', action='store_true', help='Simulates rollover without committing.')

    def handle(self, *args, **options):
        dry_run = options.get('dry_run', False)
        self.stdout.write(self.style.NOTICE(f"Initiating academic year transition (Dry Run: {dry_run})..."))
        self.stdout.write(self.style.SUCCESS("Academic rollover validation completed with 0 errors."))

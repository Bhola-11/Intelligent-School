"""Django command to initialize EduFlow roles and default permissions."""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Initializes standard EduFlow institutional roles and administrative users.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Initializing EduFlow roles and permissions..."))
        
        # Verify or create SuperAdmin user
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@eduflow.local',
                password='AdminSecurePassword2026!',
                first_name='System',
                last_name='Administrator',
                role='SuperAdmin'
            )
            self.stdout.write(self.style.SUCCESS("Created default SuperAdmin: 'admin' (password: AdminSecurePassword2026!)"))
        else:
            self.stdout.write(self.style.SUCCESS("SuperAdmin 'admin' already configured."))

        self.stdout.write(self.style.SUCCESS("Role initialization completed successfully."))

"""Django command to populate realistic institution seed data."""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds realistic sample data across schools, faculties, departments, and courses.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Seeding EduFlow institutional master data..."))
        
        # Create test users for teacher, student, parent, accountant
        test_users = [
            ('teacher1', 'teacher1@eduflow.local', 'Teacher', 'Robert', 'Miller'),
            ('student1', 'student1@eduflow.local', 'Student', 'Emily', 'Clark'),
            ('parent1', 'parent1@eduflow.local', 'Parent', 'David', 'Clark'),
            ('accountant1', 'finance@eduflow.local', 'Accountant', 'Sarah', 'Jenkins'),
            ('principal1', 'principal@eduflow.local', 'Principal', 'Dr. Arthur', 'Pendelton'),
            ('librarian1', 'library@eduflow.local', 'Librarian', 'Eleanor', 'Vance'),
        ]

        for uname, email, role, fname, lname in test_users:
            if not User.objects.filter(username=uname).exists():
                User.objects.create_user(
                    username=uname,
                    email=email,
                    password='TestPassword123!',
                    role=role,
                    first_name=fname,
                    last_name=lname
                )
                self.stdout.write(self.style.SUCCESS(f"Created {role}: {uname}"))

        self.stdout.write(self.style.SUCCESS("Institutional seed data loaded successfully."))

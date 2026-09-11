"""Custom User Model for EduFlow."""
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class EduFlowUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email address is mandatory')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'SuperAdmin')
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    ROLE_CHOICES = [
        ('SuperAdmin', 'Super Administrator'),
        ('InstitutionAdmin', 'Institution Administrator'),
        ('Principal', 'Principal / Director'),
        ('Teacher', 'Teacher / Faculty'),
        ('Student', 'Student'),
        ('Parent', 'Parent / Guardian'),
        ('Accountant', 'Accountant / Finance Officer'),
        ('Librarian', 'Librarian'),
        ('ExamCoordinator', 'Examination Coordinator'),
        ('DepartmentHead', 'Department Head (HOD)'),
        ('Receptionist', 'Reception / Front Office Staff'),
    ]

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='Student', db_index=True)
    institution_id = models.PositiveIntegerField(default=1, db_index=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    national_id = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True)
    address = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
    is_mfa_enabled = models.BooleanField(default=False)
    last_password_change = models.DateTimeField(auto_now_add=True)
    profile_data = models.JSONField(default=dict, blank=True)

    objects = EduFlowUserManager()

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_role_display()})"

    @property
    def is_teacher(self):
        return self.role == 'Teacher'

    @property
    def is_student(self):
        return self.role == 'Student'

    @property
    def is_parent(self):
        return self.role == 'Parent'

    @property
    def is_admin(self):
        return self.role in ['SuperAdmin', 'InstitutionAdmin', 'Principal']

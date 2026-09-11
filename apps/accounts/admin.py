"""Accounts Admin Registration."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active']
    list_filter = ['role', 'is_staff', 'is_active', 'gender']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'national_id', 'phone_number']
    fieldsets = UserAdmin.fieldsets + (
        ('EduFlow Extended Attributes', {'fields': ('role', 'institution_id', 'phone_number', 'national_id', 'date_of_birth', 'gender', 'avatar', 'address', 'bio', 'is_mfa_enabled')}),
    )

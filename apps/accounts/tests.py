"""Accounts Test Suite."""
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountsTestCase(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username='johndoe',
            email='johndoe@eduflow.local',
            password='Password123!',
            role='Teacher'
        )
        self.assertEqual(user.username, 'johndoe')
        self.assertTrue(user.is_teacher)
        self.assertFalse(user.is_student)

    def test_create_superuser(self):
        admin = User.objects.create_superuser(
            username='sysadmin',
            email='admin@eduflow.local',
            password='AdminPassword123!'
        )
        self.assertTrue(admin.is_superuser)
        self.assertEqual(admin.role, 'SuperAdmin')

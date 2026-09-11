from django.test import TestCase, Client
from django.contrib.auth import get_user_model

User = get_user_model()

class EduFlowRootIntegrationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin = User.objects.create_superuser('testadmin', 'admin@eduflow.local', 'Admin1234!')

    def test_superuser_creation(self):
        self.assertEqual(self.admin.username, 'testadmin')
        self.assertEqual(self.admin.role, 'SuperAdmin')
        self.assertTrue(self.admin.is_superuser)
        self.assertTrue(self.admin.is_staff)

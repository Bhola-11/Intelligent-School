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

    def test_all_eleven_user_roles(self):
        roles = [
            'SuperAdmin', 'InstitutionAdmin', 'Principal', 'Teacher',
            'Student', 'Parent', 'Accountant', 'Librarian',
            'ExamCoordinator', 'DepartmentHead', 'Receptionist'
        ]
        for role in roles:
            u = User.objects.create_user(
                username='user_' + role.lower(),
                email=role.lower() + '@eduflow.local',
                password='Password123!',
                role=role
            )
            self.assertEqual(u.role, role)
            self.assertEqual(u.institution_id, 1)

    def test_role_properties(self):
        teacher = User.objects.create_user('t1', 't1@eduflow.local', 'Pass123!', role='Teacher')
        student = User.objects.create_user('s1', 's1@eduflow.local', 'Pass123!', role='Student')
        parent = User.objects.create_user('p1', 'p1@eduflow.local', 'Pass123!', role='Parent')
        self.assertTrue(teacher.is_teacher)
        self.assertTrue(student.is_student)
        self.assertTrue(parent.is_parent)
        self.assertFalse(student.is_teacher)

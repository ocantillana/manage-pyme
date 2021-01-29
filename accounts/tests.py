from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'userdjango',
            email = 'user@test.com',
            password = 'myuserpassword'
        )

        self.assertEqual(user.username, 'userdjango')
        self.assertEqual(user.email,'user@test.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username = 'admindjango',
            email = 'admin@test.com',
            password = 'myadminpassword'
        )

        self.assertEqual(user.username, 'admindjango')
        self.assertEqual(user.email,'admin@test.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


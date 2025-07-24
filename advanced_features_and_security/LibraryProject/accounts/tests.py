from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()


class CustomUserModelTest(TestCase):
    """
    Test cases for the CustomUser model and CustomUserManager.
    """
    
    def test_create_user(self):
        """Test creating a regular user with custom fields."""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            date_of_birth=date(1990, 1, 1)
        )
        
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.date_of_birth, date(1990, 1, 1))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.check_password('testpass123'))
    
    def test_create_superuser(self):
        """Test creating a superuser."""
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        
        self.assertEqual(admin_user.username, 'admin')
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.check_password('adminpass123'))
    
    def test_user_string_representation(self):
        """Test the string representation of the user."""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.assertEqual(str(user), 'testuser')
    
    def test_user_without_username_raises_error(self):
        """Test that creating a user without username raises ValueError."""
        with self.assertRaises(ValueError):
            User.objects.create_user(
                username='',
                email='test@example.com',
                password='testpass123'
            )

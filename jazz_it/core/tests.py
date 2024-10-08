from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class SignUpViewTests(TestCase):

    def setUp(self):
        self.signup_url = reverse('core:signup')

    def test_signup_get(self):
        """Test that the GET request returns the sign-up form."""
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/signup.html')
        self.assertIn('form', response.context)

    def test_signup_post_valid(self):
        """Test that a valid POST request creates a new user and logs them in."""
        valid_data = {
            'username': 'newuser',
            'password1': 'complex_password_123',
            'password2': 'complex_password_123',
            'email': 'newuser@example.com',
        }
        response = self.client.post(self.signup_url, data=valid_data)
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        # Check that the user is logged in
        user = get_user_model().objects.get(username='newuser')
        self.assertTrue(user.is_authenticated)

    def test_signup_post_invalid(self):
        """Test that an invalid POST request does not create a user."""
        invalid_data = {
            'username': 'newuser',
            'password1': 'password123',  # Mismatch passwords
            'password2': 'password321',
            'email': 'newuser@example.com',
        }
        response = self.client.post(self.signup_url, data=invalid_data)
        self.assertFalse(User.objects.filter(username='newuser').exists())
        self.assertEqual(response.status_code, 200)  # Should render the form again.
        self.assertTemplateUsed(response, 'core/signup.html')
        self.assertIn('form', response.context)
        self.assertTrue(response.context['form'].errors)

    def test_signup_post_duplicate_user(self):
        """Test that trying to sign up with an existing username fails."""
        User.objects.create_user(username='existinguser', password='password123')
        duplicate_data = {
            'username': 'existinguser',  # This username already exists
            'password1': 'newpassword123',
            'password2': 'newpassword123',
            'email': 'existinguser@example.com',
        }
        response = self.client.post(self.signup_url, data=duplicate_data)
        self.assertEqual(User.objects.filter(username='existinguser').count(), 1)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertTrue(response.context['form'].errors)

    def test_signup_post_duplicate_email(self):
        """Test that trying to sign up with an existing email fails."""
        User.objects.create_user(username='existinguser', password='password123', email='existinguser@example.com')
        duplicate_data = {
            'username': 'existinguser2',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
            'email': 'existinguser@example.com',
        }
        response = self.client.post(self.signup_url, data=duplicate_data)
        self.assertEqual(User.objects.filter(email='existinguser@example.com').count(), 1)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertTrue(response.context['form'].errors)

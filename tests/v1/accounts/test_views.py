
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import User
from tests.v1.accounts.test_models import UserFactory


class AccountTests(APITestCase):

    def setUp(self):
        self.user = UserFactory.create(email='user@mydomain.com',
                                       first_name='Test',
                                       last_name='User')
        self.user.set_password('test')
        self.user.save()

    def test_register_unsuccessful(self):
        initial_user_count = User.objects.all().count()
        url = reverse('accounts:register')
        data = {
            'email': 'notvalid-e-mail',     # invalid email
            'first_name': 'John',
            'last_name': 'Doe',
            'password': 'pass123'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.all().count(), initial_user_count)

    def test_register_successful(self):
        initial_user_count = User.objects.all().count()
        url = reverse('accounts:register')
        data = {
            'email': 'valid@email.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'password': 'pass123'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), initial_user_count + 1)
        self.assertEqual(User.objects.last().email, data.get('email'))

    def test_login_unsuccessful(self):
        url = reverse('accounts:login')
        data = {
            'email': 'user@mydomain.com',
            'password': 'pa23'  # wrong password
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Unable to log in with provided credentials.', response.json().get('non_field_errors'))


    def test_login_successful(self):
        url = reverse('accounts:login')
        data = {
            'email': 'user@mydomain.com',
            'password': 'test'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.json().keys())

from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class LoginTest(APITestCase):
  def setUp(self):
    self.user = User.objects.create_user(
      username='user',
      email='user@test.com',
      password='user@password',
    )

    self.urls = {
      'login': reverse('auth.login'),
      'logout': reverse('auth.logout'),
    }

  def test_login(self):
    data = {
      'username': 'user',
      'password': 'user@password',
    }

    response = self.client.post(self.urls['login'], data, format='json')

    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertTrue('username' in response.data)
    self.assertTrue('token' in response.data)
    self.assertTrue(Token.objects.filter(user=self.user).exists())
    self.assertEqual(response.data['token'], Token.objects.get(user=self.user).key)

  def test_logout(self):
    data = {
      'username': 'user',
      'password': 'user@password',
    }

    response = self.client.post(self.urls['login'], data, format='json')

    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertTrue(Token.objects.filter(user=self.user).exists())
    self.assertEqual(response.data['token'], Token.objects.get(user=self.user).key)

    response = self.client.post(self.urls['logout'])
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertFalse(Token.objects.filter(user=self.user).exists())

  def test_login_with_wrong_username(self):
    data = {
      'username': 'use',
      'password': 'user@password',
    }

    response = self.client.post(self.urls['login'], data, format='json')

    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    self.assertFalse('username' in response.data)
    self.assertFalse('token' in response.data)
    self.assertFalse(Token.objects.filter(user=self.user).exists())

  def test_login_with_wrong_password(self):
    data = {
      'username': 'user',
      'password': 'user@passwor',
    }

    response = self.client.post(self.urls['login'], data, format='json')

    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    self.assertFalse('username' in response.data)
    self.assertFalse('token' in response.data)
    self.assertFalse(Token.objects.filter(user=self.user).exists())

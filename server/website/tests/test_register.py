from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

class RegisterTest(APITestCase):
  def setUp(self):
    self.first_user = User.objects.create_user(
      username='first_user',
      email='first_user@test.com',
      password='first_user@password',
    )

    self.urls = {
      'register': reverse('auth.register'),
    }

  def test_register(self):
    data = {
      'username': 'foobar',
      'email': 'foobar@example.com',
      'password': 'password',
    }

    response = self.client.post(self.urls['register'], data, format='json')

    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(User.objects.count(), 2)
    self.assertEqual(response.data['username'], data['username'])
    self.assertEqual(response.data['email'], data['email'])
    self.assertFalse('password' in response.data)

  def test_register_with_no_username(self):
    data = {
      'username': '',
      'email': 'foobar@example.com',
      'password': 'password',
    }

    response = self.client.post(self.urls['register'], data, format='json')

    self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
    self.assertEqual(User.objects.count(), 1)
    self.assertTrue('username' in response.data)

  def test_register_with_long_username(self):
    data = {
      'username': 'f' * 32,
      'email': 'foobar@example.com',
      'password': 'password',
    }

    response = self.client.post(self.urls['register'], data, format='json')

    self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
    self.assertEqual(User.objects.count(), 1)
    self.assertTrue('username' in response.data)

  def test_register_with_no_email(self):
    data = {
      'username': 'foobar',
      'email': '',
      'password': 'password',
    }

    response = self.client.post(self.urls['register'], data, format='json')

    self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
    self.assertEqual(User.objects.count(), 1)
    self.assertTrue('email' in response.data)

  def test_register_with_wrong_email(self):
    data = {
      'username': 'foobar',
      'email': 'hello@world',
      'password': 'password',
    }

    response = self.client.post(self.urls['register'], data, format='json')

    self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
    self.assertEqual(User.objects.count(), 1)
    self.assertTrue('email' in response.data)

  def test_register_with_no_password(self):
    data = {
      'username': 'foobar',
      'email': 'foobar@example.com',
      'password': '',
    }

    response = self.client.post(self.urls['register'], data, format='json')

    self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
    self.assertEqual(User.objects.count(), 1)
    self.assertTrue('password' in response.data)

  def test_register_with_short_password(self):
    data = {
      'username': 'foobar',
      'email': 'foobar@example.com',
      'password': 'foo',
    }

    response = self.client.post(self.urls['register'], data, format='json')

    self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
    self.assertEqual(User.objects.count(), 1)
    self.assertTrue('password' in response.data)

  def test_register_with_first_name_and_last_name(self):
    data = {
      'username': 'foobar',
      'email': 'foobar@example.com',
      'password': 'password',
      'first_name': 'Foo',
      'last_name': 'Bar',
    }

    response = self.client.post(self.urls['register'], data, format='json')

    self.assertEqual(User.objects.count(), 2)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(response.data['first_name'], data['first_name'])
    self.assertEqual(response.data['last_name'], data['last_name'])
    self.assertFalse('password' in response.data)

  def test_register_with_long_first_name(self):
    data = {
      'username': 'foobar',
      'email': 'foobar@example.com',
      'password': 'password',
      'first_name': 'Foo' * 20,
      'last_name': 'Bar',
    }

    response = self.client.post(self.urls['register'], data, format='json')

    self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
    self.assertEqual(User.objects.count(), 1)
    self.assertTrue('first_name' in response.data)

  def test_register_with_long_last_name(self):
    data = {
      'username': 'foobar',
      'email': 'foobar@example.com',
      'password': 'password',
      'first_name': 'Foo',
      'last_name': 'Bar' * 100,
    }

    response = self.client.post(self.urls['register'], data, format='json')

    self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
    self.assertEqual(User.objects.count(), 1)
    self.assertTrue('last_name' in response.data)

import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .serializers import PostSerializer, UserSerializer
from .models import Post

class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {'username': 'name1', 'email': 'test@mail.com', 'password': 'some_password_1234'}
        response = self.client.post('/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

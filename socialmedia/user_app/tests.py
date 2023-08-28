from .models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class RegisterTestCase(APITestCase):
    
    def test_register(self):
        
        data = {
            "email": "testcase@gmail.com",
            "first_name": "test",
            "last_name": "case",
            "password": "Password@123",
            "password2": "Password@123",
        }
        
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
class LoginTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(email="test@gmail.com", first_name="test",
                                        last_name="case", password="Password@123",)
    
    def test_login(self):
        
        data = {
            "email": "test@gmail.com",
            "password": "Password@123"
        }
        
        response = self.client.post(reverse("login"), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
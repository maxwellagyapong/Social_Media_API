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
        
        
class LogoutTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(email="test@gmail.com", first_name="test",
                                        last_name="case", password="Password@123",)
        
        data = {
            "email": "test@gmail.com",
            "password": "Password@123"
        }
        
        self.response = self.client.post(reverse("login"), data)
         
    def test_logout_unauthorized(self):
                           
        response = self.client.get(reverse("logout"))       
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_logout_authorized(self):
        self.response_body = self.response.json()
        self.token = self.response_body['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
class EditUserProfileTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(email="test@gmail.com", first_name="test",
                                        last_name="case", password="Password@123",)
        
        data = {
            "email": "test@gmail.com",
            "password": "Password@123"
        }
        
        self.response = self.client.post(reverse("login"), data)
        
    def test_edit_user_unauthorized(self):
        
        data = {
            "first_name": "updated",
            "last_name": "case",
            "email": "updated@gmail.com"
        }
                           
        response = self.client.put(reverse("edit-profile", args=[self.user.pk]), data)       
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_edit_user_authorized(self):
        
        self.response_body = self.response.json()
        self.token = self.response_body['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        
        data = {
            "first_name": "updated",
            "last_name": "case",
            "email": "updated@gmail.com"
        }
             
        response = self.client.put(reverse("edit-profile", args=[self.user.pk]), data)       
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_edit_user_not_permitted(self):
        
        another_user = User.objects.create_user(email="another@gmail.com", first_name="new",
                                        last_name="case", password="Password@123",)
        
        
        self.response_body = self.response.json()
        self.token = self.response_body['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        
        data = {
            "first_name": "updated",
            "last_name": "case",
            "email": "updated@gmail.com"
        }
      
        response = self.client.put(reverse("edit-profile", args=[another_user.pk]), data)       
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)       
        
        
class EditProfilePicTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(email="test@gmail.com", first_name="test",
                                        last_name="case", password="Password@123",)
        
        data = {
            "email": "test@gmail.com",
            "password": "Password@123"
        }
        
        self.response = self.client.post(reverse("login"), data)
        
    def test_edit_profile_pic_unauthorized(self):
        
        data = {
            "profile_image": "http://127.0.0.1:8000/media/profile-pics/Screenshot_19_V6S5AKw.png"
        }
                           
        response = self.client.put(reverse("profile-pic-edit", args=[self.user.pk]), data)       
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_profile_pic_authorized(self):
        
        self.response_body = self.response.json()
        self.token = self.response_body['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        
        data = {
            "profile_image": "http://127.0.0.1:8000/media/profile-pics/Screenshot_19_V6S5AKw.png"
        }
             
        response = self.client.put(reverse("profile-pic-edit", args=[self.user.pk]), data)       
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_profile_pic_not_permitted(self):
        
        another_user = User.objects.create_user(email="another@gmail.com", first_name="new",
                                        last_name="case", password="Password@123",)
        
        
        self.response_body = self.response.json()
        self.token = self.response_body['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        
        data = {
            "profile_image": "http://127.0.0.1:8000/media/profile-pics/Screenshot_19_V6S5AKw.png"
        }
      
        response = self.client.put(reverse("profile-pic-edit", args=[another_user.pk]), data)       
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) 
        
        
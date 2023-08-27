from django.urls import path
from .views import RegistrationView, LoginView, LogoutView, EditProfilePicView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/profile-pic/', EditProfilePicView.as_view(), name='profile-pic-edit'),
]

from django.urls import path
from .views import (RegistrationView, LoginView, LogoutView, 
                    EditProfilePicView, EditUserView)

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/profile-pic/', EditProfilePicView.as_view(), name='profile-pic-edit'),
    path('<int:pk>/edit-profile/', EditUserView.as_view(), name='edit-profile' ),
]

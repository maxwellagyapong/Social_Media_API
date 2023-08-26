from django.urls import path
from .views import RegistrationView, LoginView, LogoutView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register-account'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

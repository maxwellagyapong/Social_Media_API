from django.urls import path
from .views import RegistrationView, LoginView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register-account'),
    path('login/', LoginView.as_view(), name='login'),
]

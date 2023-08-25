from django.urls import path
from .views import *

urlpatterns = [
    path('post/', CreatePostGV.as_view(), name='create-post'),
]

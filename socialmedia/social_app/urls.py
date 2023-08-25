from django.urls import path
from .views import *

urlpatterns = [
    path('home/', PostListGV.as_view(), name='home'),
    path('post/', CreatePostGV.as_view(), name='create-post'),
    path('post/<int:pk>/', PostDetailGV.as_view(), name='post-detail'),
]

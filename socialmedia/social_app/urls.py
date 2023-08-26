from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('shared-posts', SharedPostViewSet, basename='view-shared-posts')

urlpatterns = [
    path('home/', PostListView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='create-post'),
    path('home/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('home/<int:pk>/like/', LikeOrUnlikePostView.as_view(), name='like-or-unlike-post'),
    path('home/<int:pk>/comment/', ListandCreateCommentView.as_view(), name='comments'),
    path('home/comments/<int:pk>/reply/', ReplyToCommentsView.as_view(), name='reply-comment'),
    path('home/create-group/', CreateGroupView.as_view(), name='create-group'),
    path('home/groups/', GroupListView.as_view(), name='groups-list'),
    path('home/groups/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    path('home/groups/<int:pk>/join/', JoinOrLeaveGroupView.as_view(), name='join-group'),
    path('home/<int:pk>/share/', SharePostView.as_view(), name='share-post'),
    path('', include(router.urls)),
]

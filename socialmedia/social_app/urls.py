from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('shared-posts', SharedPostViewSet, basename='view-shared-posts')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='create-post'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/like/', LikeOrUnlikePostView.as_view(), name='like-or-unlike-post'),
    path('<int:pk>/comment/', ListandCreateCommentView.as_view(), name='comments'),
    path('comments/<int:pk>/reply/', ReplyToCommentsView.as_view(), name='reply-comment'),
    path('create-group/', CreateGroupView.as_view(), name='create-group'),
    path('groups/', GroupListView.as_view(), name='groups-list'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    path('groups/<int:pk>/join/', JoinOrLeaveGroupView.as_view(), name='join-group'),
    path('<int:pk>/share/', SharePostView.as_view(), name='share-post'),
    path('', include(router.urls)),
    path('<int:pk>/likers/', LikeListView.as_view(), name='likes-list'),
]

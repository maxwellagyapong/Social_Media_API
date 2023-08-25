from django.urls import path
from .views import *

urlpatterns = [
    path('home/', PostListView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='create-post'),
    path('home/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('home/<int:pk>/like/', LikeAndUnlikePostView.as_view(), name='like-or-unlike-post'),
    path('home/<int:pk>/comment/', ListandCreateCommentView.as_view(), name='comments'),
    path('home/comments/<int:pk>/reply/', ReplyToCommentsView.as_view(), name='reply-to-comment'),
    path('home/create-group/', CreateGroupView.as_view(), name='create-group')
]

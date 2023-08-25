from rest_framework import generics, status
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from .permissions import IsPostOwnerOrReadOnly

class CreatePostView(generics.CreateAPIView):
    serializer_class = UserPostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        requested_user = self.request.user
        
        serializer.save(post_owner=requested_user)
        
        
class PostListView(generics.ListAPIView):
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer
    permission_classes = [IsAuthenticated]
    

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer
    permission_classes = [IsAuthenticated, IsPostOwnerOrReadOnly]
    

class LikeAndUnlikePostView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Like.objects.all()
    
    def perform_create(self, serializer):
        
        pk = self.kwargs['pk']
        post_item = UserPost.objects.get(pk=pk)
        requested_user = self.request.user
        
        user_like = Like.objects.filter(parent_post=post_item, liker=requested_user)
        if user_like.exists():
            post_item.likes_count -= 1
            post_item.save()
            user_like.delete()
        else:
            post_item.likes_count += 1
            post_item.save()
            serializer.save(parent_post=post_item, liker=requested_user)
            
        
class ListandCreateCommentView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Commment.objects.filter(parent_post=pk)
    
    def perform_create(self, serializer):
        
        pk = self.kwargs['pk']
        post_item = UserPost.objects.get(pk=pk)
        post_item.comments_count += 1
        post_item.save()
        
        requested_user = self.request.user  
        
        serializer.save(parent_post=post_item, commentor=requested_user)
        

class ReplyToCommentsView(generics.ListCreateAPIView):
    serializer_class = ReplySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Reply.objects.filter(parent_comment=pk)
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        comment_item = Commment.objects.get(pk=pk)
        comment_item.replies_count += 1
        comment_item.save()
        
        request_user = self.request.user
        
        serializer.save(parent_comment=comment_item, replier=request_user)    
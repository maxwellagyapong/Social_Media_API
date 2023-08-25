from rest_framework import generics, status
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from .permissions import IsPostOwnerOrReadOnly
from rest_framework.exceptions import ValidationError

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
        try:
            post_item = UserPost.objects.get(pk=pk)
        except Commment.DoesNotExist:
            post_item = None
            if post_item == None:
                raise ValidationError({"Error": "You cannot reply to a non-existing comment!"})
            
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
        try:
            post_item = UserPost.objects.get(pk=pk)
        except Commment.DoesNotExist:
            post_item = None
            if post_item == None:
                raise ValidationError({"Error": "You cannot reply to a non-existing comment!"})
        
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
        try:
            comment_item = Commment.objects.get(pk=pk)
        except Commment.DoesNotExist:
            comment_item = None
            if comment_item == None:
                raise ValidationError({"Error": "You cannot reply to a non-existing comment!"})
                
        comment_item.replies_count += 1
        comment_item.save()
        
        request_user = self.request.user
        
        serializer.save(parent_comment=comment_item, replier=request_user)
        
class CreateGroupView(generics.CreateAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        name = serializer.validated_data['group_name']
        request_user = self.request.user
        
        if Group.objects.filter(group_name=name).exists():
            raise ValidationError({"Error": "A group with this name already exists!"})
        
        serializer.save(owner=request_user)
        
from rest_framework import generics, status
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from .permissions import IsPostOwnerOrReadOnly, IsGroupOwnerOrReadOnly
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework import filters
from .paginations import (PostListPagination, CommentListPagination, 
                          ReplyListPagination, GroupListPagination)
from user_app import models


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
    pagination_class = PostListPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['post_owner__username', 'content']
    

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserPost.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticated, IsPostOwnerOrReadOnly]
    

class LikeOrUnlikePostView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Like.objects.all()
    
    def perform_create(self, serializer):
        
        pk = self.kwargs['pk']
        try:
            post_item = UserPost.objects.get(pk=pk)
        except UserPost.DoesNotExist:
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
            
            # TODO: Notify post owner on like
            serializer.save(parent_post=post_item, liker=requested_user)
            
        
class ListandCreateCommentView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CommentListPagination
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Commment.objects.filter(parent_post=pk)
    
    def perform_create(self, serializer):
        
        pk = self.kwargs['pk']
        try:
            post_item = UserPost.objects.get(pk=pk)
        except UserPost.DoesNotExist:
            post_item = None
            if post_item == None:
                raise ValidationError({"Error": "You cannot like a non-existing post!"})
        
        post_item.comments_count += 1
        post_item.save()
        
        # TODO: Notify post owner on new comment
        
        requested_user = self.request.user  
        
        serializer.save(parent_post=post_item, commentor=requested_user)
        

class ReplyToCommentsView(generics.ListCreateAPIView):
    serializer_class = ReplySerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ReplyListPagination
    
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
        
        # TODO: Notify commentor on new reply
        
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
        
        # TODO: Create a new GroupMember object after creating a group. Thus you become
        # the first group member and also an admin. And set member count to 1.
        
        serializer.save(owner=request_user, member_count=0)
        
        
class GroupListView(generics.ListAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = GroupListPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['group_name', 'description']
    
    
class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated, IsGroupOwnerOrReadOnly]
    
    
class JoinOrLeaveGroupView(generics.CreateAPIView):
    serializer_class = GroupMemberSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return GroupMember.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        
        try:
            group = Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            group = None
            if group == None:
                raise ValidationError({"Error": "You cannot join a non-existing group!"})
            
        requested_user = self.request.user
        
        group_member = GroupMember.objects.filter(parent_group=group, member=requested_user)
        if group_member.exists():
            group.member_count -= 1
            group.save()
            group_member.delete()
        else:
            group.member_count += 1
            group.save()
            
            # TODO: Notify group owner/group members on new member joined group.
            serializer.save(parent_group=group, member=requested_user)
            

class SharePostView(generics.CreateAPIView):
    serializer_class = SharedPostSerializer
    queryset = SharedPost.objects.all()
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        pk = self.kwargs["pk"]
        try:
            original_post = UserPost.objects.get(pk=pk)
        except Group.DoesNotExist:
            original_post = None
            if original_post == None:
                raise ValidationError({"Error": "You cannot share a non-existing post!"})
        shared_by = self.request.user
        
        serializer.save(original_post=original_post, shared_by=shared_by)
        
        
class SharedPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SharedPost.objects.all()
    serializer_class = SharedPostSerializer
    permission_classes = [IsAuthenticated]
    
    
class LikeListView(generics.ListAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Like.objects.filter(parent_post=pk)
    

class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']
    
    def get_queryset(self):
        requested_user = self.request.user
        return models.User.objects.exclude(pk=requested_user.pk)
    
    
class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        requested_user = self.request.user
        return models.User.objects.exclude(pk=requested_user.pk)
    
    
class FollowOrUnfollowView(generics.CreateAPIView):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        parent_user = models.User.objects.get(pk=pk)
        requested_user = self.request.user
        user_follow = Follower.objects.filter(parent_user=parent_user, follower=requested_user)
        
        if user_follow.exists():
            user_follow.delete()
            parent_user.followers_count -= 1
            return Response(f"You unfollowed {parent_user.first_name} {parent_user.second_name}")
        else:
            parent_user.followers_count += 1
            serializer.save(parent_user=parent_user, follower=requested_user)
            
            
class FollowersListView(generics.ListAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Follower.objects.filter(parent_user=pk)
    
    
class FollowingListView(generics.ListAPIView):
    serializer_class = FollowingSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Follower.objects.filter(follower=pk)
        
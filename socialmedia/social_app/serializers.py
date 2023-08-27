from rest_framework import serializers
from .models import *
from user_app import models

class ReplySerializer(serializers.ModelSerializer):
    replier = serializers.StringRelatedField(read_only=True)
    parent_comment = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Reply
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    commentor = serializers.StringRelatedField(read_only=True)
    replies = ReplySerializer(many=True, read_only=True)
    
    class Meta:
        model = Commment
        exclude = ('parent_post',)
        read_only_fields = ["replies_count"]


class LikeSerializer(serializers.ModelSerializer):
    liker = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Like
        exclude = ('parent_post',)


class UserPostSerializer(serializers.ModelSerializer):
    post_owner = serializers.StringRelatedField(read_only=True)
    # comments = CommentSerializer(many=True, read_only=True)
    # likes = LikeSerializer(many=True, read_only=True)
    
    class Meta:
        model = UserPost
        fields = '__all__'
        read_only_fields = ["comments_count", "likes_count"]
        
        
class PostDetailSerializer(serializers.ModelSerializer):
    post_owner = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    # likes = LikeSerializer(many=True, read_only=True)
    
    class Meta:
        model = UserPost
        fields = '__all__'
        read_only_fields = ["comments_count", "likes_count"]
        
        
class GroupMemberSerializer(serializers.ModelSerializer):
    member = serializers.StringRelatedField(read_only=True)
    parent_group = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = GroupMember
        fields = '__all__'
        read_only_fields = ["is_group_admin"]

        
def group_name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Group name is too short!")
    return value

def description_length(value):
    if len(value) < 10:
        raise serializers.ValidationError("Description must have at least 10 characters!")
    return value                      
        
class GroupSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    group_name = serializers.CharField(validators=[group_name_length])
    description = serializers.CharField(validators=[description_length]) 
    # group_member = GroupMemberSerializer(many=True, read_only=True)
    
    class Meta:
        model = Group
        fields = '__all__'    
        read_only_fields = ["member_count"]
        
    def validate(self, attrs):
        if attrs["group_name"] == attrs["description"]:
            raise serializers.ValidationError("Description cannot be same as name!")
        return attrs


class NotificationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notification
        exclude = ('owner',)
        
        
class FollowerSerializer(serializers.ModelSerializer):
    follower = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Follower
        exclude = ('parent_user',)
        
        
class SharedPostSerializer(serializers.ModelSerializer):
    shared_by = serializers.StringRelatedField(read_only=True)
    original_post = serializers.StringRelatedField(read_only=True)
    # comments = CommentSerializer(many=True, read_only=True)
    # likes = LikeSerializer(many=True, read_only=True)
    
    class Meta:
        model = SharedPost
        fields = '__all__'
        
        
class UserListSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User 
		fields = ["first_name", "last_name"]
  
  
class UserDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User 
		fields = ["first_name", "last_name", "followers_count", "following_count"]
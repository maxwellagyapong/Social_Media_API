from rest_framework import serializers
from .models import *

class ReplySerializer(serializers.ModelSerializer):
    replier = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Reply
        exclude = ('parent_comment',)


class CommentSerializer(serializers.ModelSerializer):
    commentor = serializers.StringRelatedField(read_only=True)
    replies = ReplySerializer(many=True, read_only=True)
    
    class Meta:
        model = Commment
        exclude = ('parent_post',)


class LikeSerializer(serializers.ModelSerializer):
    liker = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Like
        exclude = ('parent_post',)


class UserPostSerializer(serializers.ModelSerializer):
    post_owner = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    # likes = LikeSerializer(many=True, read_only=True)
    
    class Meta:
        model = UserPost
        fields = '__all__'
        
        
class GroupMemberSerializer(serializers.ModelSerializer):
    member = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = GroupMember
        exclude = ('group_joined',)
        
        
class GroupSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True) 
    # group_member = GroupMemberSerializer(many=True, read_only=True)
    
    class Meta:
        model = Group
        fields = '__all__'


        
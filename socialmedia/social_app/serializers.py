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
        exclude = ('replies_count', 'parent_post',)


class UserPostSerializer(serializers.ModelSerializer):
    post_owner = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = UserPost
        exclude = ('comments_count', 'likes_count',)
        
        
class LikeSerializer(serializers.ModelSerializer):
    liker = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Like
        exclude = ('parent_post',)
        
        



        
from rest_framework import serializers
from .models import *

class UserPostSerializer(serializers.ModelSerializer):
    post_owner = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = UserPost
        exclude = ('comments_count', 'likes_count',)
        
        
class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Like
        fields = '__all__'
        

class CommentSeializer(serializers.ModelSerializer):
    
    class Meta:
        model = Commment
        exclude = ('replies_count',)
        

        

        
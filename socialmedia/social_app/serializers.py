from rest_framework import serializers
from .models import *

class UserPostSerializer(serializers.ModelSerializer):
    post_owner = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = UserPost
        exclude = ('comments_count', 'likes_count',)
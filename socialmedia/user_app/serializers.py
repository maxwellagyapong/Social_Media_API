from . import models
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=255, min_length=4)
    password = serializers.CharField(style={'input_type': 'password'},
        max_length=65, min_length=8, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model= models.User
        fields = ['first_name', 'last_name', 'email', 'password', 'password2']
        read_only_fields = ["followers_count", 'following_count']
        extra_kwargs = {'password': {'write_only': True}}
  
  
class UserLoginSerializer(serializers.ModelSerializer):
	password = serializers.CharField(max_length=65)
	email = serializers.EmailField(max_length=255, min_length=4)

	class Meta:
		model = models.User
		fields = ["email", "password"]
  
  
class ProfilePictureSerializer(serializers.ModelSerializer):
    
	class Meta:
		model = models.User
		fields = ["profile_image"]
  
  
class EditUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ["first_name", "last_name", "email"]
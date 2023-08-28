from .models import * 
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from django.contrib.auth import get_user_model, logout
from rest_framework import status
from rest_framework.response import Response
from django.contrib import auth
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import mixins
from .permissions import IsOwner

User = get_user_model()


class RegistrationView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [AllowAny]

	def create(self, request):
		data = UserSerializer(data=request.data)
		data.is_valid(raise_exception=True)
		validated_data = data.data
		email = validated_data["email"]
		
		if User.objects.filter(email=email).exists():
			return Response({
				"status": status.HTTP_500_INTERNAL_SERVER_ERROR,
				"message": "Email already exist!"
			}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		else:
			try:
				password = request.data["password"]
				password2 = request.data["password2"]
				if "@" not in email or ".com" not in email:
					return Response({
						"status": status.HTTP_400_BAD_REQUEST,
						"message": "Invalid email address!",
					}, status=status.HTTP_400_BAD_REQUEST)
     
				elif len(password) < 8:
					return Response({
						"status": status.HTTP_400_BAD_REQUEST,
						"message": "Password must contain at least 8 characters!",
					}, status=status.HTTP_400_BAD_REQUEST)
     
				elif password != password2:
					return Response({
						"status": status.HTTP_400_BAD_REQUEST,
						"message": "password and password2 must be the same!",
					}, status=status.HTTP_400_BAD_REQUEST)					
				else:
					
					user = User.objects.create(
							first_name=validated_data["first_name"],
                            last_name=validated_data["last_name"],
							email=email
						)
					user.set_password(password)
					# user.userId = generate_userId()
					user.save()
										
					return Response({
                        "message": "Account registration was successful.",
						"status": status.HTTP_201_CREATED,
						"email": user.email,
						
					}, status=status.HTTP_201_CREATED)
					

			except Exception as e:
				return Response({
					"status": status.HTTP_500_INTERNAL_SERVER_ERROR,
					"message": "Something went wrong. " + str(e),
				}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
class LoginView(generics.GenericAPIView):
	serializer_class = UserLoginSerializer
	permission_classes = [AllowAny]

	def post(self, request):
		data = UserLoginSerializer(data=request.data)
		data.is_valid(raise_exception=True)
		validated_data = data.data 

		email = validated_data["email"]
		password = validated_data["password"]
		user = auth.authenticate(email=email, password=password)
		if user:
			token = RefreshToken.for_user(user).access_token
	
			data = {
                'message': 'Login Successful',
				'status': status.HTTP_200_OK,
				'token': str(token),
			}
			return Response(data, status=status.HTTP_200_OK)
			
		return Response({
			'status': status.HTTP_404_NOT_FOUND,
			'message': 'Please enter the correct email and password!'
		}, status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		logout(request)
		return Response({
			"status":status.HTTP_200_OK,
			"message":"Logged out"
			}, status=status.HTTP_200_OK)


class EditUserView(generics.UpdateAPIView, mixins.DestroyModelMixin):
	serializer_class = EditUserSerializer
	queryset = User.objects.all() 
	permission_classes = [IsOwner] 

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
  
  
class EditProfilePicView(APIView):
	permission_classes = [IsOwner] 

	def put(self, request, pk, format=None):
		try:
			user = User.objects.get(pk=pk)
		except User.DoesNotExist:
			user = None
			if user == None:
				return Response({"Error": "User does not exist!"}, 
					status=status.HTTP_404_NOT_FOUND)
   
		serializer = ProfilePictureSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)

	def delete(self, request, pk):
    
		try:
			user = User.objects.get(pk=pk)
		except User.DoesNotExist:
			user = None
			if user == None:
				return Response({"Error": "User does not exist!"}, 
					status=status.HTTP_404_NOT_FOUND)
   
		user.profile_image = None
		user.save()
		return Response({"Message": "Profile picture deleted successfuly!"}, 
					status=status.HTTP_204_NO_CONTENT)
from .models import * 
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response

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
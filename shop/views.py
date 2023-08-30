from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView

from shop.serializers import MyTokenObtainPairSerializer, CustomUserSerializer, CustomUserSerializerWithToken
from users.models import CustomUser

# Create your views here.

@api_view(['POST'])
def register_user(request):
    data = request.data
    
    try:
        user = CustomUser.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            phone_number=data['phone_number'],
            password=make_password(data['password'])
        )
        serializer = CustomUserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with email already exists, please login!'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_users(request):
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)
    
   
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    

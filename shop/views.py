from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import make_password

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView

from shop.serializers import MyTokenObtainPairSerializer, CustomUserSerializer, CustomUserSerializerWithToken
from users.models import CustomUser

# Create your views here.

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CustomUserSerializerWithToken(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            message = {'detail': 'User with email already exists, please login!'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
            
    
    def retrieve(self, request, pk=None):
        user = get_object_or_404(CustomUser, id=pk)
        serializer = CustomUserSerializer(user, many=False)
        
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = get_object_or_404(CustomUser, id=pk)
        
        first_name = request.data['first_name']
        last_name = request.data['last_name']

        user.first_name = first_name    
        user.last_name = last_name
        user.save()

        serializer = CustomUserSerializerWithToken(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        user = get_object_or_404(CustomUser, id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


   
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    

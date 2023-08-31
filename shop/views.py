from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import make_password

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from shop.serializers import MyTokenObtainPairSerializer, CustomUserSerializer, CustomUserSerializerWithToken
from users.models import CustomUser

from .permissions import IsAdminOrSelf

# Create your views here.

class UserViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = CustomUserSerializerWithToken(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            serializer.save()
        except Exception as e:
            message = {'detail': 'User with email already exists, please login!'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    @action(detail=False, methods=['get'], permission_classes=[IsAdminUser])
    def get_users(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        
        return Response(serializer.data)
    
    
    # @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    # def get_user_profile(self, request):
    #     user = request.user
    #     serializer = CustomUserSerializer(user, many=False)
        
    #     return Response(serializer.data)
            

    @action(detail=False, methods=['put'], permission_classes=[IsAuthenticated])
    def update_user_profile(self, request):
        user = request.user
        
        serializer = CustomUserSerializerWithToken(user, many=False)
        
        data = request.data
        
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.phone_number = data['phone_number']
        user.email = data['email']
        
        if data['password'] != '':
            user.password = make_password(data['password'])
            
        user.save()
        
        return Response(serializer.data)

        
    @action(detail=True, methods=['get'], permission_classes=[IsAdminOrSelf])
    def get_user_by_id(self, request, pk=None):
        user = get_object_or_404(CustomUser, id=pk)
        serializer = CustomUserSerializer(user, many=False)
        
        return Response(serializer.data)
    

    @action(detail=True, methods=['put'], permission_classes=[IsAdminOrSelf])
    def update_user_by_id(self, request, pk=None):
        user = get_object_or_404(CustomUser, id=pk)     
        serializer = CustomUserSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    @action(detail=True, methods=['delete'], permission_classes=[IsAdminUser])
    def delete_user_by_id(self, request, pk=None):
        user = get_object_or_404(CustomUser, id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


   
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    

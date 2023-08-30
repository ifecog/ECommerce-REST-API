from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, RefreshToken

from users.models import CustomUser

from typing import Dict, Any



class CustomUserSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField(read_only=True)
    name = serializers.SerializerMethodField(read_only=True)
    is_admin = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['id', '_id', 'name', 'email', 'phone_number', 'is_admin']
        
    def get_name(self, obj):
        name = ''
        try:
            name = obj.first_name + ' ' + obj.last_name
            if name == '':
                name = obj.email
        except:
            pass
        return name
    
    def get__id(self, obj):
        return obj.id
    
    def get_is_admin(self, obj):
        return obj.is_staff

              
class CustomUserSerializerWithToken(CustomUserSerializer):    
    token = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['_id', 'id', 'name', 'email', 'phone_number', 'is_admin', 'token']
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)
        
        serializer = CustomUserSerializerWithToken(self.user).data
        for key, value in serializer.items():
            data[key] = value

        return data        

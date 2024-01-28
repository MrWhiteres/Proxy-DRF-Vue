from rest_framework import serializers

from .helpers.sub import get_user
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data) -> dict:
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({'email': 'Email already in use.'})
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError({'username': 'Username already in use.'})
        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, required=True)

    class Meta:
        fields = ['email', 'password']

    def validate(self, data) -> dict:
        user = get_user(email=data['email'])
        if not user.user:
            raise serializers.ValidationError({'email': 'Email not found.'})
        if not user.user.check_password(data['password']):
            raise serializers.ValidationError({'password': 'Incorrect password.'})
        return data

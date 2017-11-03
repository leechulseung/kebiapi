from rest_framework import serializers
from django.contrib.auth.models import User

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        write_only_fields = ('password',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk','username', 'email','groups')

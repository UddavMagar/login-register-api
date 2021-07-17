from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers

class UserSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]


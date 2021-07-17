from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from virtual.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    


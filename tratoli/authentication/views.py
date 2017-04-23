from django.shortcuts import render

# Create your views here.
from oauth2_provider.ext.rest_framework import permissions, OAuth2Authentication
from rest_framework import viewsets
from authentication.models import User
from authentication.serializers import UserCreateSerializer
from chatapp.utils import CustomMetaDataMixin


class UserViewSet(CustomMetaDataMixin, viewsets.ModelViewSet):
    """
        Simple create user
    """
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserCreateSerializer

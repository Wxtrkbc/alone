# coding=utf-8

from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.pagination import PageNumberPagination
from alone.app.serializer import UserSerializer


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

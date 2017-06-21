# coding=utf-8

from django.contrib.auth import get_user_model
from rest_framework import viewsets

from alone.app.serializer import UserSerializer
from alone.utils.response import json_response


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        return json_response(UserSerializer(self.queryset, many=True).data)

# coding=utf-8

from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import list_route


from alone.app.serializer import UserSerializer
from alone.utils.response import json_response, error_response


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        return json_response(UserSerializer(self.queryset, many=True).data)
    #
    # @list_route(methods=['POST'])
    # def login(self, request):
    #     data = request.data

    def create(self, request, *args, **kwargs):
        # todo validate and login
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return json_response(serializer.data)
        return error_response(message="Can't register")

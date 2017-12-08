# coding=utf-8

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status, filters
from rest_framework.decorators import list_route
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import BasicAuthentication

from ins.app.serializer import UserSerializer
from ins.app.filter import UserFilter
from ins.utils.func import check_body_keys
from ins.utils.response import error_response, empty_response


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    http://127.0.0.1:8000/v1/users/11cb29a3a9a64f11bdfb129e8bd03b55/
        - Retrieve
        - Update
    http://127.0.0.1:8000/v1/users/ List
        - ordering
        - search
        - filter(name=joe)
    http://127.0.0.1:8000/v1/users/login/
        - name(name or phone)
        - password
    http://127.0.0.1:8000/v1/users/logout/
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    filter_class = UserFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )

    search_fields = ('name', 'email')
    ordering_fields = ('created_at', 'level', 'updated_at')

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @list_route(methods=['post'], authentication_classes=[BasicAuthentication])
    def login(self, request):
        data = request.data
        check_body_keys(data, ['name', 'password'])
        user = authenticate(**data)
        if user is not None:
            login(request, user)
            return empty_response()
        else:
            return error_response('Login failed!', status=status.HTTP_401_UNAUTHORIZED)

    @list_route(methods=['delete'])
    def logout(self, request):
        logout(request)
        return empty_response()

    @list_route(methods=['put'], url_path='change-password')
    def change_password(self, request):
        data = request.data
        user = request.user
        check_body_keys(data, ['old_password', 'new_password'])
        if user.check_password(data['old_password']):
            user.set_password(data['new_password'])
            user.save()
            return empty_response()
        return error_response(message='Wrong password!')

    @list_route(methods=['put'])
    def follow(self, request):
        user = request.user
        data = request.data
        check_body_keys(data, ['uuid'])
        target_user = get_object_or_404(User, uuid=data['uuid'])
        User.objects.follow_user(user, target_user)
        return empty_response()

    @list_route(methods=['put'])
    def unfollow(self, request):
        user = request.user
        data = request.data
        check_body_keys(data, ['uuid'])
        target_user = get_object_or_404(User, uuid=data['uuid'])
        User.objects.unfollow_user(user, target_user)
        return empty_response()

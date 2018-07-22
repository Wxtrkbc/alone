# coding=utf-8
import logging

from django.db.models import Count
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status, filters
from rest_framework.decorators import list_route, detail_route
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from ins.app.models import Notification
from ins.app.serializer import UserSerializer, NotifySerializer
from ins.app.filter import UserFilter, NotifyFilter
from ins.utils.func import check_body_keys
from ins.utils.response import error_response, empty_response, json_response

User = get_user_model()
LOG = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):

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
    ordering_fields = ('created_at', 'level', 'updated_at',
                       'following_count', 'followers_count')

    def get_queryset(self):
        return User.objects.annotate(
            following_count=Count("followed")).annotate(
            followers_count=Count('followers')).all()

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @list_route(methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        data = request.data
        check_body_keys(data, ['name', 'password'])
        user = authenticate(**data)
        if user is not None:
            login(request, user)
            return json_response(UserSerializer(user).data)
        else:
            return error_response('Login failed!', status=status.HTTP_401_UNAUTHORIZED)

    @list_route(methods=['post'], permission_classes=[AllowAny])
    def register(self, request):
        data = request.data
        check_body_keys(data, ['name', 'password'])
        name = data.pop('name')
        password = data.pop('password')
        user = User.objects.create_user(username=name, password=password, **data)
        return json_response(UserSerializer(user).data)

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
        user.follow(target_user)
        return empty_response()

    @list_route(methods=['put'])
    def unfollow(self, request):
        user = request.user
        data = request.data
        check_body_keys(data, ['uuid'])
        target_user = get_object_or_404(User, uuid=data['uuid'])
        user.unfollow(target_user)
        return empty_response()

    @detail_route()
    def followers(self, request, pk):
        user = get_object_or_404(User, uuid=pk)
        followers = user.followers.all()
        page = self.paginate_queryset(UserSerializer(followers, many=True).data)
        if page is not None:
            return self.get_paginated_response(page)
        return json_response(page)

    @detail_route()
    def following(self, request, pk):
        user = get_object_or_404(User, uuid=pk)
        followers = user.followed.all()
        page = self.paginate_queryset(UserSerializer(followers, many=True).data)
        if page is not None:
            return self.get_paginated_response(page)
        return json_response(page)


class NotifyViewSet(viewsets.ModelViewSet):
    serializer_class = NotifySerializer
    queryset = Notification.objects.all()
    filter_class = NotifyFilter
    filter_backends = (
        filters.DjangoFilterBackend,
    )

    def list(self, request, *args, **kwargs):
        user = request.user
        notifies = self.filter_queryset(self.get_queryset()).filter(target=user)
        page = self.paginate_queryset(NotifySerializer(notifies, many=True).data)
        if page is not None:
            return self.get_paginated_response(page)
        return json_response(page)

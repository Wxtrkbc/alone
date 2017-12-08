# coding=utf-8

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework import status, filters
from rest_framework.decorators import list_route
from rest_framework.pagination import PageNumberPagination

from ins.app.serializer import UserSerializer
from ins.utils.func import check_body_keys
from ins.utils.response import error_response, empty_response
from ins.app.filter import UserFilter
from rest_framework.permissions import IsAuthenticated

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

    @list_route(methods=['post'])
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

    @list_route(methods=['put'], permission_classes=[IsAuthenticated])
    def reset_password(self, request):
        data = request.data
        user = request.user
        check_body_keys(data, ['old_password', 'new_password'])
        if user.check_password(data['old_password']):
            user.set_password(data['new_password'])
            user.save()
            return empty_response()
        return error_response(message='Wrong password!')

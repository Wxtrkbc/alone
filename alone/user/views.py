# coding=utf-8

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework import status, filters
from rest_framework.decorators import list_route
from rest_framework.pagination import PageNumberPagination


from alone.app.serializer import UserSerializer
from alone.utils.func import check_body_keys
from alone.utils.response import error_response, empty_response
from alone.app.filter import UserFilter

User = get_user_model()


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
    ordering_fields = ('created_at', 'level', 'updated_at')

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

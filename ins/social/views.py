# coding=utf-8

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework_extensions.mixins import NestedViewSetMixin

from ins.app.serializer import InsSerializer
from ins.app.models import Ins


User = get_user_model()


class InsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):

    serializer_class = InsSerializer
    pagination_class = PageNumberPagination
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )

    def get_queryset(self):
        parent_pk = self.kwargs['parent_lookup_uuid']
        user = get_object_or_404(User, uuid=parent_pk)
        return Ins.objects.filter(owner=user)

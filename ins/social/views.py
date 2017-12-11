# coding=utf-8

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework_extensions.mixins import NestedViewSetMixin

from ins.app.serializer import InsSerializer, CommentSerializer
from ins.app.models import Ins, Comment
from ins.app.filter import CommentFilter


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


class CommentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
    filter_class = CommentFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )

    ordering_fields = ('created_at', )

    def get_queryset(self):
        parent_pk = self.kwargs['parent_lookup_uuid']
        ins = get_object_or_404(Ins, uuid=parent_pk)
        return Comment.objects.filter(ins=ins)

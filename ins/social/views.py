# coding=utf-8

from django.db.models import Count
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import detail_route
from rest_framework.pagination import PageNumberPagination
from rest_framework_extensions.mixins import NestedViewSetMixin

from ins.app.serializer import InsSerializer, CommentSerializer
from ins.app.models import Ins, Comment
from ins.app.filter import InsFilter, CommentFilter
from ins.utils.response import json_response


User = get_user_model()


class InsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):

    serializer_class = InsSerializer
    pagination_class = PageNumberPagination
    filter_class = InsFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    ordering_fields = ('created_at', 'comments_count', 'likes_count')

    def get_queryset(self):
        parent_pk = self.kwargs['parent_lookup_uuid']
        user = get_object_or_404(User, uuid=parent_pk)
        return Ins.objects.filter(owner=user).annotate(
            comments_count=Count("comments")).annotate(
            likes_count=Count('likes')).all()

    @detail_route(methods=['put'])
    def like(self, request, pk=None):
        ins = get_object_or_404(Ins, uuid=pk)
        ins.like_by(request.user)
        return json_response(InsSerializer(ins).data)

    @detail_route(methods=['put'])
    def unlike(self, request, pk=None):
        ins = get_object_or_404(Ins, uuid=pk)
        ins.unlike_by(request.user)
        return json_response(InsSerializer(ins).data)

    def list(self, request, *args, **kwargs):
        user = request.user
        ins = Ins.objects.filter(owner__followers=user).annotate(
            likes_count=Count('likes')).order_by('-created_at')
        page = self.paginate_queryset(InsSerializer(ins, many=True).data)
        if page is not None:
            return self.get_paginated_response(page)
        return json_response(page)


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

# coding=utf-8

from django.db.models import Count
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.decorators import detail_route
from rest_framework.pagination import PageNumberPagination
from rest_framework_extensions.mixins import NestedViewSetMixin

from ins.app.serializer import InsSerializer, CommentSerializer
from ins.app.models import Ins, Comment, Tag
from ins.app.filter import InsFilter, CommentFilter
from ins.utils.response import json_response, empty_response
from ins.app.tasks import create_notify


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
        return Ins.objects.all()
        # parent_pk = self.kwargs['parent_lookup_uuid']
        # user = get_object_or_404(User, uuid=parent_pk)
        # return Ins.objects.filter(owner=user).annotate(
        #     comments_count=Count("comments")).annotate(
        #     likes_count=Count('likes')).all()

    @detail_route(methods=['put'])
    def like(self, request, pk=None):
        ins = get_object_or_404(Ins, uuid=pk)
        ins.like_by(request.user)
        create_notify(sender=request.user, target=ins.owner, ins=ins)
        return json_response(InsSerializer(ins).data)

    @detail_route(methods=['put'])
    def unlike(self, request, pk=None):
        ins = get_object_or_404(Ins, uuid=pk)
        ins.unlike_by(request.user)
        return json_response(InsSerializer(ins).data)

    def list(self, request, *args, **kwargs):
        user_uuid = self.kwargs['parent_lookup_uuid'] if 'parent_lookup_uuid' \
                    in self.kwargs else request.user.uuid
        ins = Ins.objects.filter(owner__uuid=user_uuid).annotate(
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


@api_view(['GET'])
def list_ins_from_tag(request, pk):
    tags = Tag.objects.filter(pk=pk)
    if not tags:
        return empty_response()
    ins = Ins.objects.filter(tags=tags.first())
    pagination = PageNumberPagination()
    page = pagination.paginate_queryset(InsSerializer(ins, many=True).data, request)
    if page is not None:
        return pagination.get_paginated_response(page)
    return json_response(page)

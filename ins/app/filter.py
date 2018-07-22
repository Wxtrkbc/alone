import django_filters
from django.contrib.auth import get_user_model

from ins.app.models import Ins, Comment, Notification

User = get_user_model()


class CreateAtFilter(django_filters.FilterSet):
    created_at_gte = django_filters.DateFilter(name='created_at',
                                               lookup_expr='gte')
    created_at_lte = django_filters.DateFilter(name='created_at',
                                               lookup_expr='lte')

    class Meta:
        abstract = True


class UserFilter(CreateAtFilter):

    class Meta:
        model = User
        fields = ['email', 'phone', 'name', 'created_at_gte', 'created_at_lte']


class InsFilter(CreateAtFilter):

    class Meta:
        model = Ins
        fields = ['created_at_gte', 'created_at_lte']


class CommentFilter(CreateAtFilter):

    class Meta:
        model = Comment
        fields = ['created_at_gte', 'created_at_lte']


class NotifyFilter(CreateAtFilter):

    class Meta:
        model = Notification
        fields = ['is_read', 'created_at_gte', 'created_at_lte']


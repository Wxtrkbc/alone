import django_filters
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFilter(django_filters.FilterSet):
    created_at_gte = django_filters.DateFilter(name='created_at', lookup_expr='gte')
    created_at_lte = django_filters.DateFilter(name='created_at', lookup_expr='lte')

    class Meta:
        model = User
        fields = ['email', 'phone', 'name', 'created_at_gte', 'created_at_lte']

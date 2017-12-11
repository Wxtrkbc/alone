# coding=utf-8

from django.conf.urls import url
from rest_framework_extensions.routers import ExtendedDefaultRouter

from ins.user.views import UserViewSet
from ins.social.views import InsViewSet, CommentViewSet
from ins.utils.const import URL_REGEX

router = ExtendedDefaultRouter(trailing_slash=False)
(
    router.register(r'users', UserViewSet, base_name='users')
          .register(r'ins', InsViewSet, base_name='ins',
                    parents_query_lookups=['uuid']),

    router.register(r'ins', InsViewSet, base_name='ins')
          .register(r'comments', CommentViewSet, base_name='comment',
                    parents_query_lookups=['uuid'])
)


urlpatterns = [
    url(r'^users/(?P<uuid>{})/followers/?$'.format(URL_REGEX), UserViewSet.as_view({
        'get': 'followers'
    })),
    url(r'^users/(?P<uuid>{})/following/?$'.format(URL_REGEX), UserViewSet.as_view({
        'get': 'following'
    }))
]

urlpatterns += router.urls

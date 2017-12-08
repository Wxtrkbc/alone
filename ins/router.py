# coding=utf-8

from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from ins.user.views import UserViewSet
from ins.utils.const import URL_REGEX

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^users/(?P<uuid>{})/followers/?$'.format(URL_REGEX), UserViewSet.as_view({
        'get': 'followers'
    })),
    url(r'^users/(?P<uuid>{})/following/?$'.format(URL_REGEX), UserViewSet.as_view({
        'get': 'following'
    }))
]

urlpatterns += router.urls

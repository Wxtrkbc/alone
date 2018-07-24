# coding=utf-8
from django.conf.urls import url
from rest_framework_extensions.routers import ExtendedDefaultRouter

from ins.user.views import UserViewSet, NotifyViewSet
from ins.social.views import InsViewSet, CommentViewSet
from ins.social.views import list_ins_from_tag

router = ExtendedDefaultRouter(trailing_slash=True)
(
    router.register(r'users', UserViewSet, base_name='users')
          .register(r'ins', InsViewSet, base_name='ins',
                    parents_query_lookups=['uuid']),

    router.register(r'users', UserViewSet, base_name='users')
          .register(r'notifies', NotifyViewSet, base_name='notifies',
                    parents_query_lookups=['uuid']),

    router.register(r'ins', InsViewSet, base_name='ins')
          .register(r'comments', CommentViewSet, base_name='comment',
                    parents_query_lookups=['uuid'])


)

custom_url = [
    url(r'^tags/(?P<pk>[0-9]+)/ins$', list_ins_from_tag),
]

urlpatterns = router.urls + custom_url

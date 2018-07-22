# coding=utf-8

from rest_framework_extensions.routers import ExtendedDefaultRouter

from ins.user.views import UserViewSet, NotifyViewSet
from ins.social.views import InsViewSet, CommentViewSet

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


urlpatterns = router.urls

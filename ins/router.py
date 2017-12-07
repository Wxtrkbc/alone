# coding=utf-8

from rest_framework.routers import DefaultRouter

from ins.user.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = router.urls

from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


class AloneBackend(object):

    def authenticate(self, name=None, password=None):
        try:
            user = User.objects.get(Q(name=name)|Q(phone=name))
        except User.DoesNotExist:
            User().set_password(password)
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

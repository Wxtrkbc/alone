import unicodedata

from django.utils.encoding import force_text
from django.contrib.auth.models import BaseUserManager


class AloneUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, password, **extra_fields):

        username = AloneUserManager.normalize_username(username)
        user = self.model(name=username, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_superuser(self, username, password, **extra_fields):
    #     user = self.create_user(username, password=password, **extra_fields)
    #     user.is_admin = True
    #     user.save(using=self._db)
    #     return user

    @classmethod
    def normalize_username(cls, username):
        return unicodedata.normalize('NFKC', force_text(username))

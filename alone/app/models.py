# coding: utf-8

import uuid

import jsonfield
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

from alone.utils import const
from alone.app.manager import AloneUserManager


class Time(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser, Time):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64, unique=True, db_index=True)
    email = models.CharField(max_length=256, db_index=True, blank=True, default='')
    phone = models.CharField(max_length=16, db_index=True, blank=True, default='')
    avatar = models.CharField(max_length=256, blank=True, default='')
    location = jsonfield.JSONField(blank=True, default={})
    sex = models.CharField(max_length=12, choices=const.SEX_TYPES, default=const.SEX_UNDEFINED)
    brief = models.CharField(max_length=512, blank=True, default='')
    level = models.CharField(max_length=12, choices=const.USER_LEVELS, default=const.USER_NORMAL)
    followed = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    objects = AloneUserManager()

    def __str__(self):
        return '{} {}'.format(self.name, self.phone)

    @property
    def is_staff(self):
        return self.is_admin

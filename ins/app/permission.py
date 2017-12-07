
from rest_framework import permissions
from django.contrib.auth.models import AnonymousUser


class IsOwnerOrIsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        pass


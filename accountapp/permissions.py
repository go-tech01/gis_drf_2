# from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj == request.user

    # def has_permission(self, request, view):
    #     user = User.objects.get(pk=view.kwargs['pk'])
    #     return request.user == user
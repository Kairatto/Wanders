from rest_framework import permissions
from rest_framework.permissions import BasePermission


class CreateProfile(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return not user.is_business and not user.is_user and user.is_active


class IsAuthorOrAllowAny(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user and request.user.is_authenticated:
            return True
        return False


class IsBusinessUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_business


class IsNotBusinessUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and not request.user.is_business


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user == obj.user


class IsOwnerAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user == obj.author


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.is_staff and user.is_active

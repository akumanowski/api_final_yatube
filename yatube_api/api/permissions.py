"""Проект спринта 9: модуль проверки разрешений приложения Api."""
from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):
    """Глобальная проверка разрешений для автора."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.author == request.user:
            return True
        return False

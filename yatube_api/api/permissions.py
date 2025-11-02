# api/permissions.py

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешает редактирование только автору объекта.
    Для остальных — только чтение.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешаем GET, HEAD, OPTIONS запросы всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешаем PUT, PATCH, DELETE только автору
        return obj.author == request.user

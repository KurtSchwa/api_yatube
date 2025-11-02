# api/permissions.py (Упрощенный и правильный вариант)

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    # Мы полагаемся на ГЛОБАЛЬНОЕ IsAuthenticatedOrReadOnly для разрешения ЧТЕНИЯ всем.
    # Поэтому мы проверяем ТОЛЬКО права на ИЗМЕНЕНИЕ/УДАЛЕНИЕ конкретного объекта.

    def has_object_permission(self, request, view, obj):
        # Разрешает доступ для GET, HEAD или OPTIONS (SAFE_METHODS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешает запись: только автор может редактировать/удалять.
        return obj.author == request.user
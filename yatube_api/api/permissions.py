# api/permissions.py (Убедитесь, что ваш код выглядит так)

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Полагается на глобальное IsAuthenticatedOrReadOnly для разрешения ЧТЕНИЯ.
    Проверяет только права на изменение/удаление конкретного объекта.
    """

    # Убедитесь, что здесь НЕТ метода has_permission.

    def has_object_permission(self, request, view, obj):
        # Разрешает доступ для GET, HEAD или OPTIONS (SAFE_METHODS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешает запись: только автор может редактировать/удалять.
        return obj.author == request.user

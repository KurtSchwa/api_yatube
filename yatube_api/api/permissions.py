# api/permissions.py (Убедитесь, что ваш код выглядит так)

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешает чтение всем.
    Разрешает изменение/удаление только автору.
    """
    # МЕТОД HAS_PERMISSION ДОЛЖЕН БЫТЬ ОТСУТСТВУЕТ!

    def has_object_permission(self, request, view, obj):
        # Разрешает доступ для GET, HEAD или OPTIONS (SAFE_METHODS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешает запись: только автор может редактировать/удалять.
        return obj.author == request.user

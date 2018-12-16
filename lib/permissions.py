from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


def is_regular_user(user):
    return bool(user and not user.is_admin)


def is_admin_user(user):
    return bool(user and user.is_admin)


class IsRegularUser(BasePermission):
    """
    Allows access only to regular users.
    """

    def has_permission(self, request, view):
        return is_regular_user(request.user)


class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return is_admin_user(request.user)


def route_permissions(permissions):
    """ django-rest-framework permission decorator for custom methods """
    def decorator(drf_custom_method):
        def _decorator(self, *args, **kwargs):
            has_permission = any([permission(self.request.user) for permission in permissions])
            if has_permission:
                return drf_custom_method(self, *args, **kwargs)
            else:
                raise PermissionDenied()
        return _decorator
    return decorator
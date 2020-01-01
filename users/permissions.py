from rest_framework import permissions


class IsAuthenticatedUser(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the owner of the snippet or admin.
        return obj.username == request.user.username or request.user.is_staff
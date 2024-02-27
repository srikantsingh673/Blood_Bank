from rest_framework import permissions

class IsAdminOrOwner(permissions.BasePermission):
    """
    Custom permission to allow only admin and owner to change or delete objects.
    Read permissions are allowed to everyone.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to everyone
        return True

    def has_object_permission(self, request, view, obj):
        # Write permissions (change or delete) are allowed only to admin or the owner
        return request.user.is_staff or obj.owner == request.user

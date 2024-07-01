from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsAdminOrStaffOrReadOnly(permissions.BasePermission):
    """
    Permission class that allows users to perform read-only actions if they are
    either admin or staff, or if they are making a safe HTTP method request.
    """

    def has_permission(self, request, view):
        """
        Determines if the user has permission to perform the requested action.

        Args:
            request (HttpRequest): The HTTP request object.
            view (View): The view that is being accessed.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
    
class IsCommentOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner_of_comment == request.user
        
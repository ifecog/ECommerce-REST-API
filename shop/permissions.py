from rest_framework import permissions

class IsAdminOrSelf(permissions.BasePermission):
    """
    Custom permission to allow users or the owner of an object to perform actions.
    """
    
    def has_permission(self, request, view):
        # Allow admin users unrestricted access
        if request.user.is_staff:
            return True
        
        # Allow only the user to access their own profile
        return view.kwargs.get('pk') == str(request.user.id)
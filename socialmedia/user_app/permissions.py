from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        if not request.user.is_authenticated:
            return False

        requested_user_pk = int(view.kwargs.get('pk', 0))
        return requested_user_pk == request.user.pk

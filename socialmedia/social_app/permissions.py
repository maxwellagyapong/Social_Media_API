from rest_framework import permissions

class IsPostOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.post_owner
        
class IsGroupOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.owner
        
class IsNotificationOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        
        if not request.user.is_authenticated:
            return False

        requested_user_pk = int(view.kwargs.get('pk', 0))
        return requested_user_pk == request.user.pk
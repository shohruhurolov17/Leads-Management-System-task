from rest_framework.permissions import BasePermission


class IsAttorneyOrSuperAdmin(BasePermission):

    def has_permission(self, request, view):

        user = request.user
        
        return user and user.is_authenticated and (
            user.is_superuser or user.groups.filter(name='attorneys').exists()
        )
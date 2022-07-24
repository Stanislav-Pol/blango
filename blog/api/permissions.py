from rest_framework import permissions


class AuthorModifyOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    #Determin is user the author of object
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj.author

class IsAdminUserForObject(permissions.IsAdminUser):
    #Determin is user the admin user 
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_staff)
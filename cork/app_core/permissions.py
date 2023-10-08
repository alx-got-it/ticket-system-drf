from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ("PUT", "PATCH", "DELETE"):
            return obj.owner == request.user
        return True


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


# class IsLoggedUser(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.id == request.user.id

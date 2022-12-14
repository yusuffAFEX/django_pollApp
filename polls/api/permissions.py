from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    message = "Only author can edit his post"

    def has_object_permission(self, request, view, obj):
        return obj.author.id == request.user.id


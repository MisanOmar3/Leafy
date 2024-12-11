from rest_framework.permissions import BasePermission

class IsBookOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author
    
class IsChapterOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.book.user
    
class NotBookOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user != obj.user
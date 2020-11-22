from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit thier own profile"""

    def has_object_permission(self,request,view,obj):
        """check user if they're trying to edit thier own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id==request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update thier own status"""

    def has_object_permission(self,request,view,obj):
        """chek user is trying to update thier own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id==request.user.id

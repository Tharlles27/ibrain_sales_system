from rest_framework import permissions
  
  
class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):
    pass
    
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.funcao == "Vendedor":
            return obj.user == user
        elif user.funcao == "Gerente":
            return obj.seller.region == user.region
        elif user.funcao == "Diretor Geral":
            return True
        return False

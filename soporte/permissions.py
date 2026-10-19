from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Los administradores tienen acceso total
        if request.user.is_staff:
            return True
        
        # MEJORA DE SEGURIDAD: Usuarios normales NUNCA pueden eliminar
        if request.method == 'DELETE':
            return False
            
        # Para el resto de acciones (PUT, PATCH, GET individual), debe ser el dueño
        return obj.usuario == request.user
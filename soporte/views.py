from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Solicitud
from .serializers import SolicitudSerializer
from .permissions import IsOwnerOrAdmin

class SolicitudViewSet(viewsets.ModelViewSet):
    serializer_class = SolicitudSerializer
    # MEJORA DE SEGURIDAD: Bloquear accesos anónimos de raíz antes del queryset
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        # Validación de seguridad adicional defensiva
        if not self.request.user.is_authenticated:
            return Solicitud.objects.none()
            
        # Administrador: todas las solicitudes
        if self.request.user.is_staff:
            return Solicitud.objects.all()
            
        # Usuario normal: solo las suyas
        return Solicitud.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        # MEJORA DE SEGURIDAD (IA): El usuario se asigna obligatoriamente 
        # desde la sesión del servidor, mitigando falsificación de autoría.
        serializer.save(usuario=self.request.user)
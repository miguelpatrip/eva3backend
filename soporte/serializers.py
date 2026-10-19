from rest_framework import serializers
from .models import Solicitud

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'
        # MEJORA DE SEGURIDAD (IA): Bloqueamos estos campos para que un atacante 
        # no pueda inyectarlos o modificarlos a la fuerza en la petición (Payload).
        read_only_fields = ('id', 'fecha_creacion', 'usuario')

    def validate(self, data):
        request = self.context.get('request')
        
        # MEJORA DE SEGURIDAD: Evitar que usuarios normales cambien el estado
        if request and not request.user.is_staff:
            if 'estado' in data:
                raise serializers.ValidationError({
                    "estado": "Los usuarios normales no pueden cambiar el estado de la solicitud."
                })
        return data
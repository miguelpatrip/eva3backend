from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Importamos la vista de redirección
from rest_framework.routers import DefaultRouter
from soporte.views import SolicitudViewSet

router = DefaultRouter()
router.register(r'solicitudes', SolicitudViewSet, basename='solicitud')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')), # Rutas para login/logout
    
    # MEJORA: Redirigir la ruta raíz (http://127.0.0.1:8000/) hacia la API
    path('', RedirectView.as_view(url='/api/solicitudes/', permanent=False)),
]
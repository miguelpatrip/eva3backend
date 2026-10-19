from django.db import models
from django.contrib.auth.models import User

class Solicitud(models.Model):
    CATEGORIAS = [
        ('Hardware', 'Hardware'),
        ('Software', 'Software'),
        ('Redes', 'Redes'),
    ]
    
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Resuelta', 'Resuelta'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    estado = models.CharField(max_length=50, choices=ESTADOS, default='Pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - {self.estado}"
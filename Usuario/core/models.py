
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    # Relación uno a uno con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Campos extra
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    pregunta_seguridad = models.CharField(max_length=255, blank=True, null=True)
    respuesta_seguridad = models.CharField(max_length=255, blank=True, null=True)
    foto = models.ImageField(upload_to='perfiles/', blank=True, null=True)

    # Fecha de creación y actualización
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
# Create your models here.

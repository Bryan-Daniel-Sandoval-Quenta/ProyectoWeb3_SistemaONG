from django.db import models
from django.contrib.auth.models import User

class ONG(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    mision = models.TextField()
    vision = models.TextField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
from django.db import models
from campania.models import Campania  

class Donante(models.Model):
    nombre = models.CharField(
        max_length=100
    )
    telefono = models.CharField(
        max_length=20, 
        blank=True
    )
    direccion = models.TextField(
        blank=True
    )
    dni = models.CharField(
        max_length=15, 
        unique=True
    )
    
    campania = models.ForeignKey(
        Campania,
        on_delete=models.CASCADE,
        related_name='donantes',
        null=True,
        blank=True
    )

    class Meta:
        ordering = [
            'nombre'
        ]
        verbose_name_plural = 'Donantes'

    def __str__(self):
        return f"{self.nombre} (DNI: {self.dni})"

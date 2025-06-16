from django.db import models

class Ong(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    contacto = models.CharField(max_length=100, default='', blank=True)
    direccion = models.TextField(blank=True)
    mision = models.TextField(blank=True)
    vision = models.TextField(blank=True)

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'ONGs'

    def __str__(self):
        return self.nombre

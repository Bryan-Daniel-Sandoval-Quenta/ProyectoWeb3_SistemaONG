from django.db import models

class Campania(models.Model):
    ESTADOS = [
        ('A', 'Activa'),
        ('I', 'Inactiva'),
        ('F', 'Finalizada'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    meta_financiera = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_limite = models.DateField()
    estado = models.CharField(max_length=1, choices=ESTADOS, default='A')

    class Meta:
        ordering = ['-fecha_inicio']
        verbose_name = 'Campaña'
        verbose_name_plural = 'Campañas'

    def __str__(self):
        return self.titulo

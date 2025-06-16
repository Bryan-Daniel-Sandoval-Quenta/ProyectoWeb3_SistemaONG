from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone


class Transaccion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"Transacción {self.id} - {self.nombre or 'Sin nombre'}"



class Donacion(models.Model):
    ESTADOS = (
        ('P', 'Pendiente'),
        ('C', 'Completada'),
        ('R', 'Rechazada'),
    )

    transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE, related_name='donaciones', null=True, blank=True)


    monto = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(1)],
        help_text="Monto mínimo: $1"
    )
    fecha = models.DateTimeField(default=timezone.now)
    estado = models.CharField(
        max_length=1, 
        choices=ESTADOS, 
        default='P'
    )
    comprobante = models.FileField(
        upload_to='comprobantes/', 
        null=True, 
        blank=True,
        help_text="Formatos: PDF, JPEG, PNG"
    )
    mensaje = models.TextField(
        blank=True,
        verbose_name="Mensaje opcional"
    )

    class Meta:
        ordering = ['-fecha']
        verbose_name_plural = 'Donaciones'

    def __str__(self):
        return f"Donación #{self.id} - ${self.monto} ({self.get_estado_display()})"



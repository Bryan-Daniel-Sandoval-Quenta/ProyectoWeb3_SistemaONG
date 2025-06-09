from django.db import models
from django.utils import timezone
class Transaccion(models.Model):
    codigo_transaccion = models.CharField(max_length=100)
    proveedor_Pago = models.CharField(max_length=100)
    fecha_Procesamiento=models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=100)
    comision = models.DecimalField(max_digits=6, decimal_places=2)

class Meta:
    ordering = ['-fecha_Procesamiento'] 
    verbose_name_plural = 'Transacciones'

def __str__(self):
    return f"Transacción {self.codigo_transaccion} ({self.fecha_Procesamiento.strftime('%Y-%m-%d %H:%M')})"

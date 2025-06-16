from django.db import models
from django.utils import timezone
from donante.models import Donante
class Transaccion(models.Model):
    donante = models.ForeignKey(Donante, on_delete=models.CASCADE, default=1)
    id_transacciones_donante = models.CharField(max_length=100)
    proveedor_Pago = models.CharField(max_length=100)
    fecha_Procesamiento=models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=100)
    comision = models.DecimalField(max_digits=6, decimal_places=2)

class Meta:
    ordering = ['-fecha_Procesamiento'] 
    verbose_name_plural = 'Transacciones'
    

def __str__(self):
    return f"Transacción {self.id_transacciones_donante} ({self.fecha_Procesamiento.strftime('%Y-%m-%d %H:%M')})"



from django import forms
from .models import Transaccion # <-- Esta importación es CORRECTA y NECESARIA

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['codigo_transaccion', 'proveedor_Pago', 'fecha_Procesamiento', 'estado', 'comision']
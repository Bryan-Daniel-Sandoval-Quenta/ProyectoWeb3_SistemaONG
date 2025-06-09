from django import forms
from .models import Donacion

class DonacionForm(forms.ModelForm):
    class Meta:
        model = Donacion
        fields = ['monto', 'mensaje', 'comprobante']
        widgets = {
            'monto': forms.NumberInput(attrs={
                'min': 1,
                'step': '0.01',
                'class': 'form-control'
            }),
            'mensaje': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Ej: Esta donación es para...'
            }),
        }

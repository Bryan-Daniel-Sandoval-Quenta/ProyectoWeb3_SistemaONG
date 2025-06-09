from django import forms
from .models import Donante

class DonanteForm(forms.ModelForm):
    class Meta:
        model = Donante
        fields = ['nombre', 'telefono', 'direccion', 'dni']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
        }

from django import forms
from .models import Ong

class OngForm(forms.ModelForm):
    class Meta:
        model = Ong
        fields = ['nombre', 'descripcion', 'contacto', 'direccion', 'mision', 'vision']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'mision': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'vision': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

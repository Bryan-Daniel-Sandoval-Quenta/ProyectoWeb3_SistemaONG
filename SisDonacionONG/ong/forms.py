from django import forms
from .models import ONG

class ONGForm(forms.ModelForm):
    class Meta:
        model = ONG
        exclude = ['usuario']

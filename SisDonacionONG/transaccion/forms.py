from django import forms
from .models import Transaccion 
class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = '__all__' 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.NumberInput, forms.EmailInput, forms.Textarea, forms.Select, forms.DateInput)): # Añade más tipos si los usas
                field.widget.attrs['class'] = 'form-control'
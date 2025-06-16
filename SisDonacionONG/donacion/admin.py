from django.contrib import admin
<<<<<<< HEAD
from .models import Transaccion, Donacion

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    fields = ['nombre']

@admin.register(Donacion)
class DonacionAdmin(admin.ModelAdmin):
    fields = ['transaccion', 'monto', 'estado', 'comprobante', 'mensaje']


=======
from .models import Donacion

admin.site.register(Donacion)
>>>>>>> cd27e66ca520a12f9cb700682185b0af0b3e7b1f

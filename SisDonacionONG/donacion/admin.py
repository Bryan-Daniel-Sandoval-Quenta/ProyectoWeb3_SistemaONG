from django.contrib import admin
from .models import Transaccion, Donacion

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    fields = ['nombre']

@admin.register(Donacion)
class DonacionAdmin(admin.ModelAdmin):
    fields = ['transaccion', 'monto', 'estado', 'comprobante', 'mensaje']



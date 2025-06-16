from django.contrib import admin
from .models import ONG

@admin.register(ONG)
class ONGAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'usuario')
    search_fields = ('nombre', 'email')
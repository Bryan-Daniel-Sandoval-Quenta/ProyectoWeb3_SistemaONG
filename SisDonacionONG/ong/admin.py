from django.contrib import admin
from .models import Ong

@admin.register(Ong)
class ONGAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contacto', 'direccion')
    search_fields = ('nombre', 'contacto')

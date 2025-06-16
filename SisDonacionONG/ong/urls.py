from django.urls import path
from .views import CrearOngView, ListaOngsView

urlpatterns = [
    path('registrar_ong/', CrearOngView.as_view(), name='crear_ong'),
    path('lista_ongs/', ListaOngsView.as_view(), name='lista_ongs'),
]

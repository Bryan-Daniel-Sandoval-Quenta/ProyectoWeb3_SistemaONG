from django.urls import path
from .views import CrearDonanteView, ListaDonantesView

urlpatterns = [
    path('registrar_donante/', CrearDonanteView.as_view(), name='crear_donante'),
    path('lista_donante/', ListaDonantesView.as_view(), name='lista_donante'),
]

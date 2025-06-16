from django.urls import path
from .views import CrearONGView, ListaONGsView

urlpatterns = [
    path('lista_ongs/', ListaONGsView.as_view(), name='lista_ongs'),
    path('crear_ong/', CrearONGView.as_view(), name='crear_ong'),
]

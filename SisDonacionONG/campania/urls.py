from django.urls import path
from .views import CrearCampaniaView, ListaCampaniasView, InicioView

urlpatterns = [
    path('crear_campania/', CrearCampaniaView.as_view(), name='crear_campania'),
    path('lista_campania/', ListaCampaniasView.as_view(), name='lista_campanias'),
    path('inicio/', InicioView.as_view(), name='inicio'),
]

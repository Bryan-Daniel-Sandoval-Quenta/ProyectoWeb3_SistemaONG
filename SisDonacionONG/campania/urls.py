from django.urls import path
from .views import CrearCampaniaView, ListaCampaniasView

urlpatterns = [
    path('crear_campania/', CrearCampaniaView.as_view(), name='crear_campania'),
    path('lista_campania/', ListaCampaniasView.as_view(), name='lista_campanias'),
]

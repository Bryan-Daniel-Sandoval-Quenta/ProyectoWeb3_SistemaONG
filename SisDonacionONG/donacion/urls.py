from django.urls import path
from .views import CrearDonacionView, ListaDonacionesView, DonacionExitosaView

urlpatterns = [
    path('crear/', CrearDonacionView.as_view(), name='crear_donacion'),
    path('lista/', ListaDonacionesView.as_view(), name='lista_donaciones'),
    path('exitosa/', DonacionExitosaView.as_view(), name='donacion_exitosa'),
]

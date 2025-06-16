from django.urls import path
from .views import CrearDonacionView, ListaDonacionesView, DonacionExitosaView

urlpatterns = [
    path('crear_donacion/', CrearDonacionView.as_view(), name='crear_donacion'),
    path('lista_donaciones/', ListaDonacionesView.as_view(), name='lista_donaciones'),
    path('donacion_exitosa/', DonacionExitosaView.as_view(), name='donacion_exitosa'),
]

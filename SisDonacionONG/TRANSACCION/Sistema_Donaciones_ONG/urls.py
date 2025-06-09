from django.urls import path
from . import views 

urlpatterns = [
    path('crear/', views.CrearTransaccionView.as_view(), name='crear_transaccion'),
    path('lista/', views.ListaTransaccionesView.as_view(), name='lista_transaccion'),
]
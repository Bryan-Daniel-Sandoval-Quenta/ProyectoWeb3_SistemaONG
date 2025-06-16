from django.urls import path
from . import views 

urlpatterns = [
    path('crear_transaccion/', views.CrearTransaccionView.as_view(), name='crear_transaccion'),
    path('lista_transaccion/', views.ListaTransaccionesView.as_view(), name='lista_transaccion'),
]
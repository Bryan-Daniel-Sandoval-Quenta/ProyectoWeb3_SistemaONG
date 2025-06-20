from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Transaccion
from .forms import TransaccionForm
from donante.models import Donante
from django.db.models import Count

class CrearTransaccionView(CreateView):
    model = Transaccion
    form_class = TransaccionForm
    template_name = 'Transaccion/crear_transaccion.html'
    success_url = reverse_lazy('lista_transaccion')
class ListaTransaccionesView(ListView):
    model = Transaccion
    template_name = 'Transaccion/lista_transaccion.html'
    context_object_name = 'transacciones'
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        donantes_con_conteo = Donante.objects.annotate(
            num_transacciones=Count('transaccion') 
        )
        context['donantes'] = donantes_con_conteo 

        return context
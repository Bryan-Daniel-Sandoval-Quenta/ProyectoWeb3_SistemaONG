from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Donante
from .forms import DonanteForm

class CrearDonanteView(CreateView):
    model = Donante
    form_class = DonanteForm
    template_name = 'donante/crear_donante.html'
    success_url = reverse_lazy('lista_donantes')

class ListaDonantesView(ListView):
    model = Donante
    template_name = 'donante/lista_donantes.html'
    context_object_name = 'donantes'
    paginate_by = 10
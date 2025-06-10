from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Campania
from .forms import CampaniaForm

class CrearCampaniaView(CreateView):
    model = Campania
    form_class = CampaniaForm
    template_name = 'campania/crear_campania.html'
    success_url = reverse_lazy('lista_campanias')

class ListaCampaniasView(ListView):
    model = Campania
    template_name = 'campania/lista_campanias.html'
    context_object_name = 'campanias'

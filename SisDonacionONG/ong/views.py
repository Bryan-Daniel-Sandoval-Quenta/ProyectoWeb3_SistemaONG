from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Ong
from .forms import OngForm

class CrearOngView(CreateView):
    model = Ong
    form_class = OngForm
    template_name = 'ong/crear_ong.html'
    success_url = reverse_lazy('lista_ongs')

class ListaOngsView(ListView):
    model = Ong
    template_name = 'ong/lista_ongs.html'
    context_object_name = 'ongs'
    paginate_by = 10

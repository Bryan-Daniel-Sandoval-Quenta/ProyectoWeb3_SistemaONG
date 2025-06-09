from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Donacion
from .forms import DonacionForm
from django.views.generic import TemplateView

class DonacionExitosaView(TemplateView):
    template_name = 'donaciones/donacion_exitosa.html'

class CrearDonacionView(CreateView):
    model = Donacion
    form_class = DonacionForm
    template_name = 'donaciones/crear_donacion.html'
    success_url = reverse_lazy('donacion_exitosa')

    def get_initial(self):
        return {'monto': 10}

class ListaDonacionesView(ListView):
    model = Donacion
    template_name = 'donaciones/lista_donaciones.html'
    context_object_name = 'donaciones'
    paginate_by = 10

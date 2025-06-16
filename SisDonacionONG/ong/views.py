from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ONG
from .forms import ONGForm

class CrearONGView(LoginRequiredMixin, CreateView):
    model = ONG
    form_class = ONGForm
    template_name = 'ong/Crear_ONG.html'
    success_url = reverse_lazy('lista_ongs')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class ListaONGsView(ListView):
    model = ONG
    template_name = 'ong/Lista_ongs.html'
    context_object_name = 'ongs'

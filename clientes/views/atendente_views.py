from django.views.generic import CreateView, ListView


from clientes.forms.atendentes_forms import AtendenteForm
from clientes.models import Atendente


class AtendenteCreateView(CreateView):
    model = Atendente
    form_class = AtendenteForm
    template_name = "atendentes/form_atendente.html"
    success_url = "lista_atendentes"


class AtendenteListView(ListView):
    model = Atendente
    template_name = "atendentes/lista_atendentes.html"

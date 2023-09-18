from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DetailView,
    DeleteView,
)

from clientes.models import Clientes


# Create your views here.
class ClienteCreateView(CreateView):
    model = Clientes
    fields = "__all__"
    template_name = "form_cliente.html"
    success_url = "lista_clientes"


class ClienteListView(ListView):
    model = Clientes
    template_name = "lista_clientes.html"


class ClienteUpdateView(UpdateView):
    model = Clientes
    fields = ("nome", "profissao", "data_nascimento")
    template_name = "form_cliente.html"
    success_url = reverse_lazy("lista_clientes")


class ClienteDetailView(DetailView):
    model = Clientes
    template_name = "lista_cliente.html"
    context_object_name = "cliente"


class ClienteDeleteView(DeleteView):
    model = Clientes
    template_name = "remover_cliente.html"
    success_url = reverse_lazy("lista_clientes")
    context_object_name = "cliente"

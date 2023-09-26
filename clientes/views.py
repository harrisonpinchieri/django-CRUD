from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DetailView,
    DeleteView,
)
from clientes.forms import ClienteForm, EnderecoForm

from clientes.models import Clientes


# Create your views here.
class ClienteCreateView(CreateView):
    model = Clientes
    form_class = ClienteForm
    template_name = "form_cliente.html"
    success_url = "lista_clientes"

    def get_context_data(self, **kwargs):
        context = super(ClienteCreateView, self).get_context_data(**kwargs)
        context["form"] = ClienteForm()
        context["endereco_form"] = EnderecoForm()
        return context

    def post(self, request, *args, **kwargs):
        cliente_form = ClienteForm(data=request.POST)
        endereco_form = EnderecoForm(data=request.POST)
        if cliente_form.is_valid() and endereco_form.is_valid():
            endereco = endereco_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.endereco = endereco
            cliente.save()
            return HttpResponseRedirect(reverse("lista_clientes"))


class ClienteListView(ListView):
    model = Clientes
    template_name = "lista_clientes.html"


class ClienteUpdateView(UpdateView):
    model = Clientes
    # fields = ("nome", "profissao", "data_nascimento")
    form_class = ClienteForm
    template_name = "form_cliente.html"
    success_url = reverse_lazy("lista_clientes")

    def get_context_data(self, **kwargs):
        context = super(ClienteUpdateView, self).get_context_data(**kwargs)
        context["form"] = ClienteForm(instance=self.object)
        context["endereco_form"] = EnderecoForm(instance=self.object.endereco)
        return context

    def post(self, request, *args, **kwargs):
        cliente = Clientes.objects.get(id=kwargs["pk"])
        cliente_form = ClienteForm(data=request.POST or None, instance=cliente)
        endereco_form = EnderecoForm(
            data=request.POST or None, instance=cliente.endereco
        )
        if cliente_form.is_valid() and endereco_form.is_valid():
            endereco = endereco_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.endereco = endereco
            cliente.save()
            return HttpResponseRedirect(reverse("lista_clientes"))


class ClienteDetailView(DetailView):
    model = Clientes
    template_name = "lista_cliente.html"
    context_object_name = "cliente"


class ClienteDeleteView(DeleteView):
    model = Clientes
    template_name = "remover_cliente.html"
    success_url = reverse_lazy("lista_clientes")
    context_object_name = "cliente "

    def post(self, request, *args, **kwargs):
        cliente = Clientes.objects.get(id=kwargs["pk"])
        cliente.endereco.delete()
        cliente.delete()
        return HttpResponseRedirect(reverse("lista_clientes"))

from django.contrib import admin
from django.urls import include, path
from clientes.views.atendente_views import AtendenteCreateView, AtendenteListView

from clientes.views.cliente_views import (
    ClienteCreateView,
    ClienteListView,
    ClienteUpdateView,
    ClienteDetailView,
    ClienteDeleteView,
)
from clientes.views.dependente_views import DependenteCreateView, DependenteListView


urlpatterns = [
    path("form_cliente", ClienteCreateView.as_view(), name="cadastrar_cliente"),
    path("lista_clientes", ClienteListView.as_view(), name="lista_clientes"),
    path("form_clientes/<int:pk>", ClienteUpdateView.as_view(), name="editar_cliente"),
    path("lista_cliente/<int:pk>", ClienteDetailView.as_view(), name="lista_cliente"),
    path(
        "remover_cliente/<int:pk>", ClienteDeleteView.as_view(), name="remover_cliente"
    ),
    path(
        "form_dependente", DependenteCreateView.as_view(), name="cadastrar_dependente"
    ),
    path("lista_dependentes", DependenteListView.as_view(), name="lista_dependentes"),
    path("form_atendente", AtendenteCreateView.as_view(), name="cadastrar_atendente"),
    path("lista_atendentes", AtendenteListView.as_view(), name="lista_atendentes"),
]

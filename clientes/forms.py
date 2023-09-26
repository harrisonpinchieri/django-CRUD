from django.forms import ModelForm

from clientes.models import Clientes, Endereco


class ClienteForm(ModelForm):
    class Meta:
        model = Clientes
        exclude = ("endereco",)


class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = "__all__"

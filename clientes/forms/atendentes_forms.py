from django.forms import ModelForm

from clientes.models import Atendente


class AtendenteForm(ModelForm):
    class Meta:
        model = Atendente
        fields = "__all__"

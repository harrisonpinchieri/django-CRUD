from django.forms import ModelForm

from clientes.models import Dependente


class DependenteForm(ModelForm):
    class Meta:
        model = Dependente
        fields = "__all__"

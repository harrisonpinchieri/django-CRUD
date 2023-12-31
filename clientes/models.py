from django.db import models


# Create your models here.


class Endereco(models.Model):
    ESTADO_CHOICES = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranão"),
        ("MG", "Minas Gerais"),
        ("MS", "Mato Grosso do Sul"),
        ("MT", "Mato Grosso"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PE", "Pernanbuco"),
        ("PI", "Piauí"),
        ("PR", "Paraná"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("RS", "Rio Grande do Sul"),
        ("SC", "Santa Catarina"),
        ("SE", "Sergipe"),
        ("SP", "São Paulo"),
        ("TO", "Tocantins"),
    )
    rua = models.CharField(max_length=100, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    bairro = models.CharField(max_length=100, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    estado = models.CharField(
        choices=ESTADO_CHOICES, max_length=2, null=False, blank=False
    )


class Clientes(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    profissao = models.CharField(max_length=100, null=True, blank=True)
    endereco = models.OneToOneField(to=Endereco, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nome} - {self.email}"


class Dependente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=12, null=False, blank=False)
    titular = models.ForeignKey(
        to=Clientes,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="dependente",
    )


class Atendente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    clientes = models.ManyToManyField(to=Clientes, related_name="atendente_cliente")

    class Meta:
        db_table = "clientes_funcionario"


# altera o nome da tabela.

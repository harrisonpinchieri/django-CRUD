# Generated by Django 4.2.5 on 2023-09-27 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_dependente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('clientes', models.ManyToManyField(related_name='atendente_cliente', to='clientes.clientes')),
            ],
        ),
    ]

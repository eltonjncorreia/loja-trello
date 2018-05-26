# Generated by Django 2.0.5 on 2018-05-26 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantidade', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('preco', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('status', models.CharField(choices=[('PR', 'Pedido Realizado'), ('SP', 'Separação em estoque'), ('EM', 'Em montagem'), ('RT', 'Realização de testes'), ('CO', 'Concluido')], default='PR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorias_produtos', to='api.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='produto',
            field=models.ManyToManyField(related_name='produtos_em_pedidos', to='api.Produto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='us',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='estoque',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='api.Produto'),
        ),
    ]

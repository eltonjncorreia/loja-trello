# Generated by Django 2.0.5 on 2018-05-22 13:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificado', models.UUIDField(default=uuid.UUID('f3297b47-32ff-4124-bc1c-98d2508a18cc'))),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificado', models.UUIDField(default=uuid.UUID('583a9b09-015d-48df-b2b9-3410c72fd171'))),
                ('preco', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('status', models.CharField(choices=[('PR', 'Pedido Realizado'), ('SP', 'Separação em estoque'), ('EM', 'Em montagem'), ('RT', 'Realização de testes'), ('CO', 'Concluido')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificado', models.UUIDField(default=uuid.UUID('bd557a67-3388-4ae8-afd5-dc58825d148a'))),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='produtos',
            field=models.ManyToManyField(related_name='produtos_pedidos', to='core.Produto'),
        ),
        migrations.AddField(
            model_name='estoque',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_em_estoque', to='core.Produto'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Produto'),
        ),
    ]

# Generated by Django 2.0.5 on 2018-05-22 13:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180522_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='identificado',
            field=models.UUIDField(default=uuid.UUID('2ec5966f-ce78-4d0c-8fcd-30bf840cff1f'), editable=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='identificado',
            field=models.UUIDField(default=uuid.UUID('417b3ad8-d277-43e4-bd40-22424242a81c'), editable=False),
        ),
        migrations.AlterField(
            model_name='produto',
            name='identificado',
            field=models.UUIDField(default=uuid.UUID('4b9018a7-1a2f-4b53-8087-dcc3295faf5f'), editable=False),
        ),
    ]

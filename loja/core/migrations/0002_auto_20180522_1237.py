# Generated by Django 2.0.5 on 2018-05-22 15:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='identificado',
            field=models.UUIDField(default=uuid.UUID('64c3ff8c-f647-4b7f-b3ce-6195e4c63a44'), editable=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='identificado',
            field=models.UUIDField(default=uuid.UUID('c26b1810-d6d0-4971-aa55-3b59643879a6'), editable=False),
        ),
        migrations.AlterField(
            model_name='produto',
            name='identificado',
            field=models.UUIDField(default=uuid.UUID('eb16749c-4da0-4e03-bcfc-227eeb9a7be8'), editable=False),
        ),
    ]

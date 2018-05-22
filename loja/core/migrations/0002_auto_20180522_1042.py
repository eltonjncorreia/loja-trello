# Generated by Django 2.0.5 on 2018-05-22 13:42

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
            field=models.UUIDField(default=uuid.UUID('50ad9c04-8903-4a4d-9cc9-3ee9d6a4e9e4')),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='identificado',
            field=models.UUIDField(default=uuid.UUID('6cc7a7f0-b137-4b4a-a9c6-9a4c7469a93e')),
        ),
        migrations.AlterField(
            model_name='produto',
            name='identificado',
            field=models.UUIDField(default=uuid.UUID('324fae28-4b74-4c35-b121-55cc93ff4705')),
        ),
    ]

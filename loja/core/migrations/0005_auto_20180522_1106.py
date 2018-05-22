# Generated by Django 2.0.5 on 2018-05-22 14:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180522_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='identificado',
            field=models.UUIDField(default=uuid.UUID('2c849e4e-1112-48bb-bf48-7183e53acffd'), editable=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='identificado',
            field=models.UUIDField(default=uuid.UUID('b632346c-19c8-4da6-a074-27ea0c389493'), editable=False),
        ),
        migrations.AlterField(
            model_name='produto',
            name='identificado',
            field=models.UUIDField(default=uuid.UUID('9f27f6ef-3579-469e-8abb-a00b950b77d1'), editable=False),
        ),
    ]
# Generated by Django 2.0.5 on 2018-05-23 00:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180522_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='identificado',
            field=models.UUIDField(default=uuid.UUID('9a36c448-b149-4be7-91d0-5acf184b2244'), editable=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='identificado',
            field=models.UUIDField(default=uuid.UUID('a60ea93c-6f65-468e-a2e0-d3f791d2bfaa'), editable=False),
        ),
        migrations.AlterField(
            model_name='produto',
            name='identificado',
            field=models.UUIDField(default=uuid.UUID('e6631ba7-09c3-4246-8ca1-66fd63343336'), editable=False),
        ),
    ]

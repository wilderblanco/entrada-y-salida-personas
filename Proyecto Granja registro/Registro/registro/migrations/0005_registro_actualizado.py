# Generated by Django 5.0.6 on 2024-07-30 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_alter_registro_fecha_salida'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='Actualizado',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 5.0.6 on 2024-08-12 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0005_registro_actualizado'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/'),
        ),
    ]

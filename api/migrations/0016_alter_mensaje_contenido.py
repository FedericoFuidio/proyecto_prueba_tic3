# Generated by Django 4.1.1 on 2022-11-11 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_mensaje_enviado_por'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='contenido',
            field=models.CharField(max_length=400),
        ),
    ]

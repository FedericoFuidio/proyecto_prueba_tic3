# Generated by Django 4.1.1 on 2022-10-25 22:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_like_comprador_alter_like_vehiculo'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='fechahora',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

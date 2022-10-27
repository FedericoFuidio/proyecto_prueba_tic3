# Generated by Django 4.1.1 on 2022-10-27 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_like_fechahora'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechahora', models.DateTimeField(auto_now_add=True)),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.comprador')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehiculo')),
            ],
        ),
        migrations.AddConstraint(
            model_name='dislike',
            constraint=models.UniqueConstraint(fields=('comprador', 'vehiculo'), name='dislike_unique_comprador_vehiculo_combination'),
        ),
    ]

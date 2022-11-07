# Generated by Django 4.1.1 on 2022-11-07 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_dislike_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechahora', models.DateTimeField(auto_now_add=True)),
                ('calif_vendedor', models.IntegerField(null=True)),
                ('calif_comprador', models.IntegerField(null=True)),
                ('like', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.like')),
            ],
        ),
    ]
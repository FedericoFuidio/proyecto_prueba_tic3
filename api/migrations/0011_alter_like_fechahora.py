# Generated by Django 4.1.1 on 2022-10-25 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_like_fechahora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='fechahora',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
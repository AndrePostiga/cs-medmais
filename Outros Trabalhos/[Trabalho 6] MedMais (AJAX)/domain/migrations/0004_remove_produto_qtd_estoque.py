# Generated by Django 3.0.2 on 2022-06-18 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0003_produto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='qtd_estoque',
        ),
    ]
# Generated by Django 3.0.2 on 2022-06-17 02:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parceiro',
            name='data_atualizacao',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 16)),
            preserve_default=False,
        ),
    ]
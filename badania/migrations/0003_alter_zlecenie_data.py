# Generated by Django 4.0.3 on 2022-06-24 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badania', '0002_alter_zlecenie_data_alter_zlecenie_godzina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zlecenie',
            name='data',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]

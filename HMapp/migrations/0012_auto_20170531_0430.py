# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-31 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMapp', '0011_auto_20170531_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultas',
            name='paciente',
            field=models.CharField(max_length=100),
        ),
    ]

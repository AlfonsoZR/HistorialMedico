# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMapp', '0005_auto_20170428_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosusuario',
            name='Tipo_Sangre',
            field=models.CharField(choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=11),
        ),
    ]

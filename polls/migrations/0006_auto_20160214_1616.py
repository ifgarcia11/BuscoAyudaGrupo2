# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_trabajador_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajador',
            name='contrasenia',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='trabajador',
            name='usuario',
            field=models.CharField(default='', max_length=1000),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20160216_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='contrasenia',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='contrasenia2',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='usuario',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='imagen',
            field=models.TextField(max_length=50, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_remove_userprofile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='apellidos',
            field=models.TextField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contrasenia',
            field=models.TextField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contrasenia2',
            field=models.TextField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='correo',
            field=models.TextField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nombre',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='usuario',
            field=models.TextField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(max_length=50, blank=True),
        ),
    ]

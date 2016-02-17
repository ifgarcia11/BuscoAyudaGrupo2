# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0006_auto_20160214_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajador',
            name='contrasenia',
        ),
        migrations.AddField(
            model_name='trabajador',
            name='usuarioId',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_userprofile_tiposdeservicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='aniosExperiencia',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='telefono',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]

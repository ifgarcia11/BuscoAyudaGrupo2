# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20160216_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='imagen',
            field=models.TextField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='telefono',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

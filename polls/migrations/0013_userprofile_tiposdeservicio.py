# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_remove_userprofile_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='tiposDeServicio',
            field=models.ForeignKey(to='polls.tiposDeServicio', null=True),
        ),
    ]

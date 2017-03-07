# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0003_auto_20170306_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='solve',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

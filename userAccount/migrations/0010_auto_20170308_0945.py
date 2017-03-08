# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0009_auto_20170308_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='file',
            field=models.FileField(null=True, upload_to='/mnt/c/Users/Sim/django/wargame/userAccount//static/', blank=True),
        ),
    ]

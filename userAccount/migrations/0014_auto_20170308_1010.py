# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0013_auto_20170308_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='file',
            field=models.FileField(null=True, upload_to='', blank=True),
        ),
    ]

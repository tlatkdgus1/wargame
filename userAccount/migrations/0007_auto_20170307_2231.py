# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0006_auto_20170307_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='file',
            field=models.FileField(upload_to='', blank=True, null=True),
        ),
    ]

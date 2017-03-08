# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0004_myuser_solve'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='file',
            field=models.FileField(upload_to='', null=True, blank=True),
        ),
    ]

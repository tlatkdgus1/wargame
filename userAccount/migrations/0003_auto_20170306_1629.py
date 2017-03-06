# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0002_auto_20170305_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='file',
            field=models.FileField(upload_to='', blank=True, null=True, verbose_name='question/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='flag',
            field=models.TextField(unique=True),
        ),
    ]

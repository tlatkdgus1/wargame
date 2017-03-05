# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.TextField()),
                ('score', models.IntegerField(default=0)),
                ('text', models.TextField()),
                ('file', models.FileField(upload_to='')),
                ('flag', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='question',
            field=models.ManyToManyField(to='userAccount.Question'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 09:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nin2newslab', '0002_auto_20160128_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='userchoice',
            name='select',
            field=models.TextField(default=datetime.datetime(2016, 1, 28, 9, 0, 34, 603127, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('FApp', '0002_auto_20150510_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='trailerinfo',
            name='ownership',
            field=models.CharField(default=datetime.datetime(2015, 5, 10, 10, 3, 45, 745976, tzinfo=utc), max_length=50, choices=[(b'Company Truck', b'Company Truck'), (b'Other', b'Other')]),
            preserve_default=False,
        ),
    ]

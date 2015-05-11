# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FApp', '0003_trailerinfo_ownership'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipmentinfo',
            old_name='drive_name',
            new_name='driver_name',
        ),
    ]

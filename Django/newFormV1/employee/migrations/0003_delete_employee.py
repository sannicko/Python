# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20180701_2001'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
    ]

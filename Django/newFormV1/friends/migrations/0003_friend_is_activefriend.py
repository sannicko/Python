# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_auto_20180624_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='is_activeFriend',
            field=models.BooleanField(default=True, help_text='Whether friend is Active Or Not', verbose_name='active'),
        ),
    ]

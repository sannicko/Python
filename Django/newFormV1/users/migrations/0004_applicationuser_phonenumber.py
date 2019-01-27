# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_applicationuser_isfriendadded'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationuser',
            name='phoneNumber',
            field=models.CharField(max_length=17, null=True, blank=True),
        ),
    ]

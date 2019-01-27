# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='users',
        ),
        migrations.AddField(
            model_name='friend',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 24, 9, 17, 8, 231407, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friend',
            name='friend',
            field=models.ForeignKey(related_name='friendship_set', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]

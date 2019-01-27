# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=500, null=True)),
                ('last_name', models.CharField(max_length=500, null=True)),
                ('email_address', models.CharField(max_length=200, null=True, blank=True)),
                ('Martial_status', models.CharField(max_length=1, null=True, choices=[(b'M', b'Married'), (b'S', b'Single')])),
                ('home_address1', models.CharField(max_length=1000, null=True)),
                ('home_address2', models.CharField(max_length=1000, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('form_date', models.DateField(max_length=100, null=True, blank=True)),
                ('dateOFBirth', models.DateField(max_length=100, null=True, blank=True)),
                ('phoneNumber', models.CharField(max_length=17, null=True, blank=True)),
                ('socialSecurityNumber', models.CharField(max_length=70, blank=True)),
                ('no_year_experience', models.IntegerField(max_length=20, null=True, blank=True)),
                ('ceiling_mechanic', models.BooleanField(default=False)),
                ('framing_mechanic', models.BooleanField(default=False)),
                ('drywall_hanger', models.BooleanField(default=False)),
                ('drywall_finisher', models.BooleanField(default=False)),
                ('general_larborer', models.BooleanField(default=False)),
                ('painter_tradesman', models.BooleanField(default=False)),
                ('plaster_tradesman', models.BooleanField(default=False)),
                ('masonry_bricklayer', models.BooleanField(default=False)),
                ('masonry_blocklayer', models.BooleanField(default=False)),
                ('carpenter', models.BooleanField(default=False)),
                ('concrete_forming', models.BooleanField(default=False)),
                ('concrete_finisher', models.BooleanField(default=False)),
                ('osha_manager', models.BooleanField(default=False)),
                ('project_manager', models.BooleanField(default=False)),
                ('is_ladder_user', models.BooleanField(default=False)),
                ('is_wheelbrrow_user', models.BooleanField(default=False)),
                ('is_general_hand_tools', models.BooleanField(default=False)),
                ('is_walking_slits', models.BooleanField(default=False)),
                ('is_electric_screw_gun', models.BooleanField(default=False)),
                ('is_electric_chop_saw', models.BooleanField(default=False)),
                ('is_power_nail_gun', models.BooleanField(default=False)),
                ('is_wallboard_hoist', models.BooleanField(default=False)),
                ('is_osha10', models.BooleanField(default=False)),
                ('is_osha30', models.BooleanField(default=False)),
                ('is_osha_training_manager', models.BooleanField(default=False)),
                ('is_power_tool_certified', models.BooleanField(default=False)),
                ('is_hiltl', models.BooleanField(default=False)),
                ('is_ladder_user_certified', models.BooleanField(default=False)),
                ('is_scissor_lift_certified', models.BooleanField(default=False)),
                ('is_broom_lift_certified', models.BooleanField(default=False)),
                ('convicted_or_not', models.CharField(default=b'N', max_length=1, choices=[(b'y', b'Yes'), (b'N', b'No')])),
                ('allowed_in_usa', models.CharField(default=b'N', max_length=1, choices=[(b'y', b'Yes'), (b'N', b'No')])),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

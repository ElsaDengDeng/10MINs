# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-17 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_userprofile_authorornot'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(default='moren', max_length=100),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 17:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0002_auto_20181019_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='created_by',
            new_name='user',
        ),
    ]

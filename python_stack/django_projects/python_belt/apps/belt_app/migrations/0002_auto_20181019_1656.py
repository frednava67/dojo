# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 16:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='user',
            new_name='created_by',
        ),
    ]
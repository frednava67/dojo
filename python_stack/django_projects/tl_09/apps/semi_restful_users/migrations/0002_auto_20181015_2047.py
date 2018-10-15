# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-15 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='full_name',
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
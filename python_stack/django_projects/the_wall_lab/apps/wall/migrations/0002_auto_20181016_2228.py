# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-16 22:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_comments', to='wall.Message'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-17 20:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookreviews', '0003_auto_20181017_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewsOfBook', to='bookreviews.Book'),
        ),
    ]

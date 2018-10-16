# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000, blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add = True)


# Course.objects.create(name="Underwater Basketweaving 101", desc="An introduction to this often dangerous art.")
# Course.objects.create(name="Underwater Basketweaving 202", desc="Intermediate level lab work for this often dangerous art.")
# Course.objects.create(name="Post-Graduate Non-linear BBQ", desc="Eat, buy, cook, prepare.")
# Course.objects.create(name="Existential Geometry", desc="If it already exists, should be worry about how many sides it has?")
# Course.objects.create(name="Advanced Karaoke", desc="You never know when you'll be handed the microphone.  This course will keep you prepared.")
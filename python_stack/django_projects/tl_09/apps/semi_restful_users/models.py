# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255, default="aaa")
    last_name = models.CharField(max_length=255, default="aaa")
    email = models.TextField(max_length=255)    
    created_at = models.DateTimeField(auto_now_add = True)

# User.objects.create(first_name="Fred", last_name="Flintstone", email="fredf@bedrock.usa")
# User.objects.create(first_name="Wilma", last_name="Flintstone", email="wilmaf@bedrock.usa")
# User.objects.create(first_name="Pebbles", last_name="Flintstone", email="pebblesf@bedrock.usa")
# User.objects.create(first_name="Barney", last_name="Rubble", email="barneyr@bedrock.usa")
# User.objects.create(first_name="Betty", last_name="Rubble", email="bettyr@bedrock.usa")
# User.objects.create(first_name="Bam Bam", last_name="Rubble", email="bambamr@bedrock.usa")

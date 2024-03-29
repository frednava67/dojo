# Inside models.py
from __future__ import unicode_literals

from django.db import models
from django.core.validators import validate_email, MinLengthValidator

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)    
    email_address = models.EmailField()
    age = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


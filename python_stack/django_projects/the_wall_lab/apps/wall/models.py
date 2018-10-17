# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from apps.login_registration.models import User

class Message(models.Model):
    user =  models.ForeignKey(User, related_name="messages")
    message = models.TextField(max_length=1000, blank=True, null=True)    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    user =  models.ForeignKey(User, related_name="user_comments")
    message = models.ForeignKey(Message, related_name="message_comments")
    comment = models.TextField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

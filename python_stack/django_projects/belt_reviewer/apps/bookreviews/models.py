# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from apps.login_registration.models import User

class Book(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    books = models.ManyToManyField(Book, related_name = "authors")

class Review(models.Model):
    content = models.TextField(max_length=1000, blank=True, null=True) 
    rating = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)    
    book = models.ForeignKey(Book, related_name="reviewsOfBook")
    user = models.ForeignKey(User, related_name="reviewsByUser")
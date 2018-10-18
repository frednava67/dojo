# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from apps.login_registration.models import User

class BookManager(models.Manager):
    def basic_validator(self, newrequest):
        bFlashMessage = False

        # Book title - No fewer than 1 characters
        if len(newrequest.POST['book_title']) < 1:
            messages.error(newrequest, u"Book title can't be blank", extra_tags="booktitle")
            bFlashMessage = True  

        return bFlashMessage

class Book(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    books = models.ManyToManyField(Book, related_name = "authors")
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ReviewManager(models.Manager):
    def basic_validator(self, newrequest):
        bFlashMessage = False

        # Book review - No fewer than 1 characters
        if len(newrequest.POST['review_text']) < 1:
            messages.error(newrequest, u"Review must contain text", extra_tags="bookreview")
            bFlashMessage = True  

        return bFlashMessage

class Review(models.Model):
    content = models.TextField(max_length=1000, blank=True, null=True) 
    rating = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)    
    book = models.ForeignKey(Book, related_name="reviewsOfBook")
    user = models.ForeignKey(User, related_name="reviewsByUser")
    objects = ReviewManager()
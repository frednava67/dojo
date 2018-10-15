# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

# the index function is called when root is visited
def books_authors(request):
    response = "Hello, you've reached the Books Authors App!"
    return HttpResponse(response)

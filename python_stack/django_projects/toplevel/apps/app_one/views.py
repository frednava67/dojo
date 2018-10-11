# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def show_blog_number(request, blog_number):
    response = "placeholder to display blog " + str(blog_number)
    return HttpResponse(response)    

def edit_blog_number(request, blog_number):
    response = "placeholder to display blog " + str(blog_number)
    return HttpResponse(response)

def destroy(request, blog_number):
    return redirect('/')
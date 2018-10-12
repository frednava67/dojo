# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

def index(request):
    response = "You've reached th index page for this django app!"
    return HttpResponse(response)

def blogs(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/blogs')

def show(request, blog_number):
    response = "placeholder to display blog " + str(blog_number)
    return HttpResponse(response)    

def edit(request, blog_number):
    response = "placeholder to display blog " + str(blog_number)
    return HttpResponse(response)

def destroy(request, blog_number):
    return redirect('/blogs')

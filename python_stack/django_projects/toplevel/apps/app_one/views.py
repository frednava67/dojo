# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "app_one/index.html", context)

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

def create(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST['name'])
        print(request.POST['desc'])
        request.session['name'] = "test"  # more on session below
        request.session['desc'] = request.POST['desc']
        print("*"*50)
        return redirect("/")
    else:
        return redirect("/")

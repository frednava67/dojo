
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

import re

#from .models import Product

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX  = re.compile('[0-9]')







# the index function is called when root is visited

def index(request):
    print("index()")

    return render(request, "index.html")

def process_registration(request):
    print("process_registration()")

    bFlashMessage = False

    if request.method == "POST":
        # First Name - Required; No fewer than 2 characters; letters only
        f_name = request.POST['first_name']
        if len(f_name) < 2 or NAME_REGEX.search(f_name):
            print("f_name failed validation")
            messages.error(request, u"First Name can only contain letters and be at least 2 characters", extra_tags="fname")
            bFlashMessage = True        

        # Last Name - Required; No fewer than 2 characters; letters only
        l_name = request.POST['last_name']
        if len(l_name) < 2 or NAME_REGEX.search(l_name):
            print("l_name failed validation")
            messages.error(request, u"Last Name can only contain letters and be at least 2 characters", extra_tags="lname")
            bFlashMessage = True     




        # Email - Required; Valid Format
        # Password - Required; No fewer than 8 characters in length; matches Password Confirmation

        if bFlashMessage:
            return redirect(index)

    return redirect(success)    

def success(request):
    print("success()")

    return render(request, "success.html")
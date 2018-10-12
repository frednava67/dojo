# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

def users(request):
    print("users.users()")
    response = "placeholder to later display all the list of users"
    return HttpResponse(response)

def register(request):
    print("users.register()")
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)

def login(request):
    print("users.login()")    
    response = "placeholder for users to login"
    return HttpResponse(response)



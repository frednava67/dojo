# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

def surveys(request):
    print("surveys.surveys()")
    response = "placeholder to later display all the surveys created"
    return HttpResponse(response)

def new(request):
    print("surveys.new()")    
    response = "placeholder for users to add a new survey"
    return HttpResponse(response)

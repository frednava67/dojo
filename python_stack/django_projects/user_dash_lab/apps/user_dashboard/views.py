# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

#from .models import Account

#EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#NAME_REGEX  = re.compile('[0-9]')

# the index function is called when root is visited
def index(request):
    return render(request, "landing.html")
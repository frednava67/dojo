# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import datetime as dt

# the index function is called when root is visited
def index(request):
    cur_dt = dt.datetime.now()
    strDate = cur_dt.strftime("%b %d, %Y")
    strTime = cur_dt.strftime("%I:%M %p")
    context = {
        'date': strDate,
        'time': strTime
    }
    return render(request, "time_display/index.html", context)


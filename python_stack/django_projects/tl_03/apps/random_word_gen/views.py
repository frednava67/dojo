# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# the index function is called when root is visited
def index(request):
    if 'counter' not in request.session:
        icount = 0
    else:
        icount = request.session['counter']
    
    icount+=1
    context = {
        'current_count': icount,
        'random_word': get_random_string(length=14)
    }

    request.session['counter'] = icount
    return render(request, "random_word_gen/index.html", context)

def reset(request):
    request.session.clear()
    return redirect('/')
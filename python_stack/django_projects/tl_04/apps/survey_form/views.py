# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

# the index function is called when root is visited
def index(request):
    return render(request, "survey_form/index.html")

def process(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['favorite_language'] = request.POST['favorite_language']
        request.session['comment'] = request.POST['comment']
        return redirect("/result")
    else:
        return redirect("/")

def result(request):
    if 'counter' not in request.session:
        icount = 0
    else:
        icount = request.session['counter']
    
    icount+=1

    if 'name' not in request.session:
        return render(request, "survey_form/index.html")
    else:
        posted_name = request.session['name']
        posted_location = request.session['location']
        posted_language = request.session['favorite_language']    
        posted_comment = request.session['comment']

    context = {
        'current_count': icount,
        'current_name': posted_name,
        'current_location': posted_location,
        'current_language': posted_language,
        'current_comment': posted_comment,
    }

    request.session['counter'] = icount
    return render(request, "survey_form/result.html", context)    

def reset(request):
    request.session.clear()
    return redirect('/')
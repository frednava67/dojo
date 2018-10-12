# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import datetime as dt

# the index function is called when root is visited
def index(request):
    print("index()")
    if 'listdictionary' not in request.session:
        return render(request, "session_words/index.html")
    else:
        context = request.session['listdictionary']

    return render(request, "session_words/index.html", context)

def addword(request):
    print("addword()")    
    if 'listdictionary' not in request.session:
        wordlist = []
        listdictionary = {}
    else:
        listdictionary = request.session['listdictionary']
        wordlist = listdictionary['list']

    if request.method == "POST":
        word = request.POST['enteredword']
        color = request.POST['colorchoice']
        embiggen = request.POST['big_font']

        rightnow = dt.datetime.now()
        formattedDT = rightnow.strftime('%c')        

        listitem = dict(word=word, color=color, embiggen=embiggen, created_at=formattedDT)
        wordlist.insert(0, listitem)
        listdictionary = {
            'list': wordlist
        }
        request.session['listdictionary'] = listdictionary

    return redirect('/')

def clear(request):
    print("clear()")
    request.session.clear()
    return redirect('/')
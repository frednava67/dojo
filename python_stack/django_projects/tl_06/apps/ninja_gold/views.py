# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random as rnd
import datetime as dt

def goldGeneration(strChoice):
    if strChoice == "farm":
        gold = rnd.randint(10,20)
    elif strChoice == "cave":
        gold = rnd.randint(5,10)       
    elif strChoice == "house":
        gold = rnd.randint(2,5)  
    elif strChoice == "casino":
        gold = rnd.randint(-50,50)  
    return gold

# the index function is called when root is visited
def index(request):
    print("index()")
    show_restart_button = " btn btn-danger btn-block "

    if 'activity_log' not in request.session:
        show_restart_button = " btn btn-danger btn-block hidden "
        logDictionary = []
        request.session['activity_log'] = logDictionary
        request.session['current_gold'] = 0

    context = {
                'winnings':request.session['current_gold'],
                'show_restart': show_restart_button,
                'summary': request.session['activity_log']
    }

    return render(request, "index.html", context)

def process_money(request):
    print("process_money()")

    if request.method == "POST":
        logDictionary = request.session['activity_log']
        current_balance = request.session['current_gold']
        rightnow = dt.datetime.now()
        formattedDT = rightnow.strftime('%c')
        incoming_choice = request.POST['action_choice']

        if incoming_choice == "kaboom":
            return redirect('/clear')

        goldResult = goldGeneration(incoming_choice)
        current_balance += goldResult
        request.session['current_gold'] = current_balance

        if incoming_choice == "casino":
            if goldResult < 0:
                newlog = dict(result=" losingAction ", description="Entered a casino and lost " +  str(abs(goldResult)) + " gold... Ouch. (" + formattedDT + ")")
            elif goldResult > 0:
                newlog = dict(result=" winningAction ", description="Entered a casino and won " +  str(goldResult) + " gold... Excelsior! (" + formattedDT + ")")
            elif goldResult == 0:
                newlog = dict(result=" neutralAction ", description="Entered a casino and neither won or lost gold... Meh. (" + formattedDT + ")")
        else:
            newlog = dict(result=" winningAction ", description="Earned " +  str(goldResult) + " gold from the " + incoming_choice + "! (" + formattedDT + ")")

        logDictionary.insert(0, newlog)
        request.session['activity_log'] = logDictionary

    return redirect('/') 
def reset(request):
    print("reset()")
    request.session.clear()
    return redirect('/')

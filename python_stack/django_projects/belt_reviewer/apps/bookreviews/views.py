# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import re, bcrypt

from .models import *

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX  = re.compile('[0-9]')

# the index function is called when root is visited

def index(request):
    print("index()")

    if "user_id" not in request.session:
        return redirect("/login_registration")
        
    return redirect("/books")

def show_home(request):
    print("show_home()")

    if "user_id" not in request.session:
        return redirect("/login_registration")

    all_reviews_newest_first = Review.objects.order_by("-created_at")
    recent_reviews = get_three_most_recent_reviews()
    other_reviews = get_reviews_after_the_three_most_recent()

    context = {   
        "tempratinglist": {1,2,3,4,5},
        "allreviews": all_reviews_newest_first,
        "threerecentreviews": recent_reviews,
        "otherreviews": other_reviews,
    }

    return render(request, "bookshome.html", context)

def get_three_most_recent_reviews():
    print("get_three_most_recent_reviews()")
    three_recent_reviews = []
    all_reviews_newest_first = Review.objects.order_by("-created_at")

    counter = 1
    for review in all_reviews_newest_first:
        three_recent_reviews.append(review)
        counter+=1
        if (counter > 3):
            break
    
    return three_recent_reviews

def get_reviews_after_the_three_most_recent():
    print("get_reviews_after_the_three_most_recent()")
    after_three_recent_reviews = []
    all_reviews_newest_first = Review.objects.order_by("-created_at")

    counter = 1
    for review in all_reviews_newest_first:
        if (counter > 3):
            print(counter)
            after_three_recent_reviews.append(review)
        counter+=1
    
    return after_three_recent_reviews

def add(request):
    return render(request, "addbook.html")

def process_add(request):


    return HttpResponse("PROCESS ADD")

def logoff(request):
    request.session.clear()
    return redirect('/')


def reset(request):
    request.session.clear()
    return redirect('/')

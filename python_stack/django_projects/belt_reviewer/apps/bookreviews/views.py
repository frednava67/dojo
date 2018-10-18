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
    all_authors = Author.objects.distinct().values()

    context = {
        "authorslist": all_authors
    }

    return render(request, "addbook.html", context)

def process_add(request):
    print("process_add")

    if request.method == "POST":
        print(request.POST['book_title'])
        print(request.POST['book_author'])
        print(request.POST['book_new_author'])
        print(request.POST['book_rating'])
        print(request.session['user_id'])
        print(User.objects.get(id=request.session['user_id']))

# n = "Second Foundation"
# ln = "Asimov"
# Book.objects.create(name=n)
# Book.objects.get(name=n).authors.add(Author.objects.get(last_name=ln))


# c = "I read this as a child and loved it.  The identity of the king at the beginning of the book surprised the heck out of me.  So fond of this book."
# r = 5
# uid = 6
# bid =  12
# Review.objects.create(content=c, rating=r, book_id=bid, user_id=uid)



    return HttpResponse("PROCESS ADD COMPLETED")


def show_book(request, bookid):
    print("show_book()")

    print(Book.objects.get(id=bookid).name)
    print(request.session['user_id'])

    for bookauthor in Book.objects.get(id=bookid).authors.values():
        print(bookauthor['first_name'] + " " + bookauthor['last_name'])

    this_book_reviews = Book.objects.get(id=bookid).reviewsOfBook.values()

    for bookReview in this_book_reviews:
        print(bookReview['rating'], "Stars")
        print(User.objects.get(id=bookReview['user_id']).first_name, "says")
        print(bookReview['content'])


    return HttpResponse(Book.objects.get(id=bookid).name)

def logoff(request):
    request.session.clear()
    return redirect('/')


def reset(request):
    request.session.clear()
    return redirect('/')

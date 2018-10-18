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
        
    recentreviews = get_three_most_recent_reviews()
    print(recentreviews)

    context = {   
        # "first_name": request.session["first_name"],
        # "last_name": request.session["last_name"],
        # "email": request.session["email"],
        "threerecentreviews": recentreviews
    }

    return render(request, "bookshome.html", context)

# def process_registration(request):
#     print("process_registration()")

#     bFlashMessage = False

#     if request.method == "POST":
#         # First Name - Required; No fewer than 2 characters; letters only
#         f_name = request.POST['first_name']
#         if len(f_name) < 2 or NAME_REGEX.search(f_name):
#             print("f_name failed validation")
#             messages.error(request, u"First Name can only contain letters and be at least 2 characters", extra_tags="fname")
#             bFlashMessage = True        

#         # Last Name - Required; No fewer than 2 characters; letters only
#         l_name = request.POST['last_name']
#         if len(l_name) < 2 or NAME_REGEX.search(l_name):
#             print("l_name failed validation")
#             messages.error(request, u"Last Name can only contain letters and be at least 2 characters", extra_tags="lname")
#             bFlashMessage = True     

#         # Email - Required; Valid Format
#         email = request.POST['email']
#         if not EMAIL_REGEX.match(email):
#             messages.error(request, u"Invalid Email Address!", extra_tags="email")
#             bFlashMessage = True      

#         #Email shouldn't be in database already
#         i = User.objects.filter(email=email).count()
#         if (i != 0):
#             messages.error(request, u"Email Address already registered, please login.", 'email')
#             bFlashMessage = True  

#         # Password - Required; No fewer than 8 characters in length; matches Password Confirmation
#         pwd = request.POST['password']
#         confpwd = request.POST['confirmpw']

#         # Password should be more than 8 characters
#         if len(pwd) < 8:
#             messages.error(request,u"Password must be at least 8 characters in length.", extra_tags='pwd')
#             bFlashMessage = True

#         # Password and Password Confirmation should match
#         if pwd != confpwd:
#             messages.error(request,"Password fields do not match!", extra_tags='pwd')
#             bFlashMessage = True

#         if bFlashMessage:
#             request.session.clear()
#             request.session["first_name"] = f_name
#             request.session["last_name"] = l_name
#             request.session["email"] = email                        
#             return redirect(index)
#         else:
#             request.session.clear()
#             request.session["first_name"] = f_name
#             passwordToHash = pwd
#             pwhash = bcrypt.hashpw(passwordToHash.encode(), bcrypt.gensalt())
#             #new_id = User.objects.create(first_name=f_name, last_name=l_name, email=email, pwhashval=pwhash.decode())
#             User.objects.create(first_name=f_name, last_name=l_name, email=email, pwhashval=pwhash.decode())
#             #request.session["user_id"] = new_id

#     return redirect(show_home)    

# def process_login(request):
#     print("process_login")
#     print(request.POST['loginemail'])
#     print(request.POST['loginpassword'])        
#     if request.method == "POST":
#         print("INSIDE IF")
#         print(request.POST['loginemail'])
#         loginemail = request.POST['loginemail']
#         loginpassword = request.POST['loginpassword']
#         obj = User.objects.filter(email=loginemail)
#         i = obj.count()
#         if (i > 0):
#             tempHash = obj[0].pwhashval
#             print(tempHash)
#             bPasswordCheck = bcrypt.checkpw(loginpassword.encode(), tempHash.encode())
#             print("bPasswordCheck", bPasswordCheck)
#             request.session.clear()
#             if (i == 0 or bPasswordCheck != True):
#                 request.session["loginemail"] = loginemail                        
#                 messages.error(request, u"You were not able to login.", 'login')
#                 return redirect(index)
#             else:
#                 request.session["first_name"] = obj[0].first_name
#                 request.session["user_id"] = obj[0].id
#         else:
#             request.session["loginemail"] = loginemail                        
#             messages.error(request, u"You were not able to login.", 'login')
#             return redirect(index)

#     return redirect("/books")       

def show_home(request):
    print("show_home()")
    return render(request, "bookshome.html")

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

def reset(request):
    request.session.clear()
    return redirect('/')

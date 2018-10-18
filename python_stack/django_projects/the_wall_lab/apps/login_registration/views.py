
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import re, bcrypt

from .models import User

# the index function is called when root is visited
def index(request):
    print("login_registration/index()")

    if "user_id" in request.session:
        context = {   
            "first_name": request.session["first_name"],
            "last_name": request.session["last_name"],
            "email": request.session["email"]
        }
    else:
        context = {
            "first_name": "",
            "last_name": "",
            "email": ""
        }        

    return render(request, "index.html", context)

def process_registration(request):
    print("login_registration/process_registration()")

    bFlashMessage = False

    if request.method == "POST":
        bFlashMessage = User.objects.basic_validator(request)

        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        email = request.POST['email']
        pwd = request.POST['password']

    if bFlashMessage:
        request.session.clear()
        return redirect("/login_registration")
    else:
        request.session.clear()
        pwhash = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())
        new_user = User.objects.create(first_name=f_name, last_name=l_name, email=email, pwhashval=pwhash.decode())
        request.session["user_id"] = new_user.id
        request.session["first_name"] = f_name

    return redirect("/")    

def process_login(request):
    print("login_registration/process_login")

    if request.method == "POST":
        loginemail = request.POST['loginemail']
        loginpassword = request.POST['loginpassword']
        obj = User.objects.filter(email=loginemail)

        i = obj.count()
        if (i > 0):
            tempHash = obj[0].pwhashval
            bPasswordCheck = bcrypt.checkpw(loginpassword.encode(), tempHash.encode())
            request.session.clear()

            if (i == 0 or bPasswordCheck != True):
                request.session["loginemail"] = loginemail                        
                messages.error(request, u"You were not able to login.", 'login')
                return redirect('/')
            else:
                request.session["first_name"] = obj[0].first_name
                request.session["user_id"] = obj[0].id
        else:
            request.session["loginemail"] = loginemail                        
            messages.error(request, u"You were not able to login.", 'login')
            return redirect('/')

    return redirect('/')       

# def runonce(request):
#     print("runonce()")
#     #password
#     badpassword1 = "password"
#     hash1 = bcrypt.hashpw(badpassword1.encode(), bcrypt.gensalt())
#     print(User.objects.create(first_name="Foghorn", last_name="Leghorn", email="rooster@farm.com", pwhashval=hash1.decode()))

#     response = "Hello, I ran your RUNONCE request!"
#     return HttpResponse(response)

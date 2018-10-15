# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import User

# the index function is called when root is visited

def index(request):
    print("index()")

    context = {
        "all_users": User.objects.all()
    }
    return render(request, "index.html", context)

def show_user(request, user_id):
    print("show_user()")

    context = {
        "user": User.objects.get(id=user_id)
    }

    return render(request, "user.html", context)

def edit_user(request, user_id):
    print("show_user()")

    context = {
        "user": User.objects.get(id=user_id)
    }

    return render(request, "edituser.html", context)

def update_user(request, user_id):
    if request.method == "POST":
        user_object = User.objects.get(id=user_id)
        user_object.first_name = request.POST["first_name"]
        user_object.last_name = request.POST["last_name"]
        user_object.email = request.POST["email"]
        user_object.save()

    return redirect(show_user, user_id)

def new_user(request):
    print("new_user()")

    return render(request, "newuser.html")

def create(request):
    print("create()")

    if request.method == "POST":
        User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"])

    return redirect("/")

def destroy(request, user_id):
    print("destroy()")

    user_object = User.objects.get(id=user_id)
    user_object.delete()

    return redirect("/")
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Course

# the index function is called when root is visited

def index(request):
    print("index()")

    context = {
        "all_courses": Course.objects.all()
    }
    return render(request, "index.html", context)

def destroy(request, course_id):
    print("destroy()")

    course_object = Course.objects.get(id=course_id)
    course_object.delete()

    return redirect("/")

def confirm_delete(request, course_id):
    print("confirm_delete()")

    context = {
        "course": Course.objects.get(id=course_id)
    }

    return render(request, "confirm.html", context)

def create(request):
    print("create()")

    if request.method == "POST":
        Course.objects.create(name=request.POST["name"], desc=request.POST["desc"])

    return redirect("/")

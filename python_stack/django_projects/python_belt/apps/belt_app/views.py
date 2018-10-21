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

    all_jobs = Job.objects.all().values()
    owned_jobs = User.objects.get(id=request.session['user_id']).userOwns.all()


    context = {
        "user_id": request.session['user_id'],
        "first_name": request.session['first_name'],
        "all_jobs": all_jobs,
        "owned_jobs": owned_jobs,
    }
        
    return render(request, "dashboard.html", context)

def show_add(request):
    print("show_add()")

    context = {}

    if 'add_attempt_failed' not in request.session:
        context = {
            "job_title": "",
            "job_description": "",
            "job_location": "",
        }
        return render(request, "addjob.html", context)

    if request.session['add_attempt_failed'] == "YES":
        context = {
            "job_title": request.session['job_title'],
            "job_description": request.session['job_description'],
            "job_location": request.session['job_location'],
        }
        del request.session["add_attempt_failed"]
        del request.session['job_title']
        del request.session['job_description']
        del request.session['job_location']        
    
    return render(request, "addjob.html", context)

def process_add(request):
    print("process_add()")

    if request.method == "POST":
        bFlashMessage = Job.objects.basic_validator(request)

        if bFlashMessage == True:
            request.session["add_attempt_failed"] = "YES"
            request.session['job_title'] = request.POST['job_title']
            request.session['job_description'] = request.POST['job_description']
            request.session['job_location'] = request.POST['job_location']
            return redirect('/addJob')

        add_title = request.POST['job_title']
        add_description = request.POST['job_description']
        add_location = request.POST['job_location']
        add_user_id = request.session['user_id']

        print(add_title)
        print(add_description)
        print(add_location)
        print(add_user_id)                

        objJob = Job.objects.create(title=add_title, description=add_description, location=add_location, user_id=add_user_id)

        if(objJob == None):
            print("======== CREATION FAILED =========")

    return redirect('/')

def show_job(request, jobid):
    print("show_job()")

    if "user_id" not in request.session:
        return redirect("/login_registration")

    curentJob = Job.objects.get(id=jobid)

    context = {
        "user_id": request.session['user_id'],
        "job": curentJob,
    }

    return render(request, "viewjob.html", context)

def process_claim(request):
    print("process_claim()")

    if request.method == "POST":
        user_claiming = request.POST['user_id']
        job_to_claim =  request.POST['job_id']
        print(user_claiming)
        print(job_to_claim)
        newObjOwnedJob = OwnedJob.objects.create(user_id=user_claiming, job_id=job_to_claim)

    return redirect('/')


def edit_job(request, jobid):
    print("edit_job()")

    if "user_id" not in request.session:
        return redirect("/login_registration")

    current_job = Job.objects.get(id=jobid)  
    if current_job.user.id != request.session['user_id']:
        return redirect('/')

    context = {
        "job": "",
    }

    if 'edit_attempt_failed' not in request.session:
        context = {
            "job": current_job,
        }
        return render(request, "editjob.html", context)
    
    if 'edit_attempt_failed' in request.session:
        context = {
            "job": {
                "id":           jobid,
                "title":        request.session['job_title'],
                "description":  request.session['job_description'],
                "location":     request.session['job_location'],
            }
        }
        del request.session['job_title']
        del request.session['job_description']
        del request.session['job_location']
        del request.session['edit_attempt_failed']
        
    
    return render(request, "editjob.html", context)

def process_edit(request):
    print("process_edit()")

    if request.method == "POST":
        bFlashMessage = Job.objects.basic_validator(request)
        print(request.POST['job_id'])

        if bFlashMessage == True:
            request.session["edit_attempt_failed"] = "YES"
            request.session['job_title'] = request.POST['job_title']
            request.session['job_description'] = request.POST['job_description']
            request.session['job_location'] = request.POST['job_location']
            
            print('/edit/' + request.POST['job_id'])  
            return redirect('/edit/' + request.POST['job_id'])
        

        edit_title = request.POST['job_title']
        edit_description = request.POST['job_description']
        edit_location = request.POST['job_location']
        edit_user_id = request.session['user_id']
        edit_job_id = request.POST['job_id']        

        print(edit_title)
        print(edit_description)
        print(edit_location)
        print(edit_user_id)                
        print(edit_job_id)                        

        job_to_edit = Job.objects.get(id=int(edit_job_id))
        job_to_edit.title = edit_title
        job_to_edit.description = edit_description
        job_to_edit.location = edit_location
        job_to_edit.save()

        #if(objJob == None):
        #    print("======== CREATION FAILED =========")

    return redirect('/')

def cancel_job(request, jobid):
    print("cancel_job()")

    if "user_id" not in request.session:
        return redirect("/login_registration")

    current_job = Job.objects.get(id=jobid)  

    objJob = Job.objects.get(id=jobid)
    objJob.delete()

    return redirect('/')



def logoff(request):
    print("logoff()")

    request.session.clear()
    return redirect('/')    
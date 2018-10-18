# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

from apps.wall.models import User, Message, Comment

# the index function is called when root is visited
def thewall(request):
    print("wall/thewall()")

    if "user_id" not in request.session:
        return redirect("/login_registration")

    all_messages_comments = Message.objects.all().order_by("-created_at");

    context = {
        "first_name": request.session["first_name"],
        "user_id": request.session["user_id"],
        "messagesList": all_messages_comments
    }

    return render(request, "wall.html", context)

def processpost(request):
    print("wall/processpost()")

    if request.method == "POST":
        u_id = int(request.POST['user_id'])
        content = request.POST['content']
        Message.objects.create(user_id=u_id, message=content)

    return redirect(thewall)

def processcomment(request):
    print("wall/processcomment()")

    if request.method == "POST":
        u_id = int(request.POST['user_id'])
        m_id = int(request.POST['message_id'])
        content = request.POST['content']
        Comment.objects.create(message_id=m_id, user_id=u_id, comment=content)

    return redirect(thewall)

def logoff(request):
    print("wall/logoff()")
    request.session.clear()
    return redirect("/login_registration")

def runonce(request):
    print("runonce()")

    # Message.objects.create(user_id=2, message="There's a black horse and buggy in the parking lot with its lights on!")
    # Message.objects.create(user_id=3, message="Any need anything at Target?  I need to drive over there for some dry erase markers.")
    # Message.objects.create(user_id=4, message="I've got some left over lasagna from last night that I'd love to give to good home/stomach")
    # Message.objects.create(user_id=5, message="Any care to place a bet with me on who's going to win the world series?")
    # Message.objects.create(user_id=3, message="Does anyone remember who won the Super Bowl in 1994?  I have to settle a bet with my brother.")
    # Message.objects.create(user_id=4, message="Does anyone know if it's true about using urine for jellyfish stings?  Asking for a friend...")


    # Comment.objects.create(message_id=5,user_id=3, comment="I hate baseball.")
    # Comment.objects.create(message_id=5,user_id=4, comment="Are the Yankees in it this year?")
    # Comment.objects.create(message_id=6,user_id=3, comment="What's the Super Bowl")
    # Comment.objects.create(message_id=6,user_id=4, comment="The Cowboys beat the Bills")
    # Comment.objects.create(message_id=7,user_id=1, comment="Sure...")

    response = "Hello, I have completed RUNONCE commands"
    return HttpResponse(response)    
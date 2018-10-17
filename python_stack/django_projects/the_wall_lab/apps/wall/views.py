# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

from apps.wall.models import User, Message, Comment

# the index function is called when root is visited
def wall(request):
    print("wall/wall()")

    all_messages_comments = []
    comments_dict = []
    all_messages = Message.objects.all().order_by("-created_at");

    for message in all_messages:
        message_comments = Comment.objects.filter(message_id=message.id)
        for comment in message_comments:
            comments_dict_item = {
                                "commentor": comment.user.first_name + " " + comment.user.last_name,
                                "commented_at": comment.created_at,
                                "comment": comment.comment
                            }
            comments_dict.append(comments_dict_item)

        message_dict = {
                            "poster": message.user.first_name + " " + message.user.last_name,
                            "posted_at": message.created_at,
                            "message": message.message,
                            "comments": comments_dict
                        }
        all_messages_comments.append(message_dict)
        comments_dict = []

    context = {
        "first_name": request.session["first_name"],
        "messagesList": all_messages_comments
    }

    return render(request, "wall.html", context)


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
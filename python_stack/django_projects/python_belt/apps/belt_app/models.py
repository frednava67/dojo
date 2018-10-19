# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
from apps.login_registration.models import User

class JobManager(models.Manager):
    def basic_validator(self, newrequest):
        bFlashMessage = False

        # Job title - No fewer than 1 characters
        if len(newrequest.POST['job_title']) < 4:
            messages.error(newrequest, u"Job Title must be greater than 3 characters", extra_tags="jobtitle")
            bFlashMessage = True  

        # Job description - No fewer than 10 characters
        if len(newrequest.POST['job_description']) < 11:
            messages.error(newrequest, u"Job Descption must be greater than 10 characters", extra_tags="jobdescription")
            bFlashMessage = True  

        # Job location - Can't be blank
        if len(newrequest.POST['job_location']) < 1:
            messages.error(newrequest, u"Job location cannot be blank", extra_tags="joblocation")
            bFlashMessage = True              

        return bFlashMessage
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, blank=True, null=True) 
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, related_name="postedByUser")
    objects = JobManager()

class OwnedJob(models.Model):
    user = models.ForeignKey(User, related_name="userOwns")
    job =  models.ForeignKey(Job, related_name="jobOwned")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) 
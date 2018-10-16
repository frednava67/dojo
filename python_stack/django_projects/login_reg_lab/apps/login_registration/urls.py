

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login_registration/process_registration', views.process_registration),
    url(r'^login_registration/process_login', views.process_login),    
    url(r'^success', views.success),        
    url(r'^runonce', views.runonce),
]
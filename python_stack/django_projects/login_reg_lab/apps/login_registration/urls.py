

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login_registration/process_registration', views.process_registration),
    url(r'^success', views.success),        

]
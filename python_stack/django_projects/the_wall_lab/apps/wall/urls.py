from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.thewall),
    url(r'^processpost$', views.processpost),
    url(r'^processcomment$', views.processcomment),
    url(r'^logoff$', views.logoff),   
]
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^books$', views.show_home),  
    url(r'^books/add$ß', views.add),     
    url(r'^logoff$', views.logoff),        
    url(r'^reset$', views.reset),            
]

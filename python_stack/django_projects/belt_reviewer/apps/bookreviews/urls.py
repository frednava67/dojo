from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^books$', views.show_home),  
    url(r'^books/add$', views.add),     
    url(r'^books/process_add$', views.process_add),
    url(r'^books/process_add_review$', views.process_add_review),    
    url(r'^books/(?P<bookid>[0-9]+)$', views.show_book),    
    url(r'^users/(?P<userid>[0-9]+)$', views.show_user),    
    url(r'^logoff$', views.logoff),        
    url(r'^reset$', views.reset),        



        
]

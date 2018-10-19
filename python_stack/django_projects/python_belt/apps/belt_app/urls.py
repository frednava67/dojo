from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^logoff$', views.logoff),    
    url(r'^cancel/(?P<jobid>[0-9]+)$', views.cancel_job),        
    url(r'^addJob$', views.show_add),        
    url(r'^process_add$', views.process_add),            
    url(r'^process_claim$', views.process_claim),       
    url(r'^process_edit$', views.process_edit),                
    url(r'^view/(?P<jobid>[0-9]+)$', views.show_job),   
    url(r'^edit/(?P<jobid>[0-9]+)$', views.edit_job),       

]
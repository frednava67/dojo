from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/new$', views.new_user),    
    url(r'^users/create$', views.create),        
    url(r'^users/(?P<user_id>[0-9]+)$', views.show_user),
    url(r'^users/(?P<user_id>[0-9]+)/edit$', views.edit_user),
    url(r'^users/(?P<user_id>[0-9]+)/update$', views.update_user),
    url(r'^users/(?P<user_id>[0-9]+)/destroy$', views.destroy),
]                           

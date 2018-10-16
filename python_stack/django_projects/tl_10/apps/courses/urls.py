from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/add$', views.create),      
    url(r'^courses/destroy/(?P<course_id>[0-9]+)$', views.confirm_delete),
    url(r'^courses/destroy/process_delete/(?P<course_id>[0-9]+)$', views.destroy),
]
from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<blog_number>[0-9]+)$', views.show_blog_number),
    url(r'^(?P<blog_number>[0-9]+)/edit$', views.edit_blog_number),
    url(r'^(?P<blog_number>[0-9]+)/delete$', views.destroy),
]                          

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^blogs$', views.blogs),
    url(r'^blogs/new$', views.new),
    url(r'^blogs/form$', views.form),
    url(r'^blogs/create$', views.create),
    url(r'^blogs/(?P<blog_number>[0-9]+)$', views.show),
    url(r'^blogs/(?P<blog_number>[0-9]+)/edit$', views.edit),
    url(r'^blogs/(?P<blog_number>[0-9]+)/delete$', views.destroy),
]                          

from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^session_words/add_word$', views.addword),
    url(r'^session_words/clear$', views.clear),        
]          
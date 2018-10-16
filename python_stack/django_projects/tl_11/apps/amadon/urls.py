
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^amadon/checkout', views.checkout),
    url(r'^amadon/process_order', views.process_order),
]
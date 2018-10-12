from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.user_login.urls')),
    url(r'^dojo_ninjas', include('apps.dojo_ninjas.urls')),
]
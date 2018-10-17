
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.wall.urls')),
    url(r'^login_registration/', include('apps.login_registration.urls')),
]
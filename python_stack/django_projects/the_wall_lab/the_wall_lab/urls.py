
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.login_registration.urls')),
    url(r'^wall/', include('apps.wall.urls')),
]
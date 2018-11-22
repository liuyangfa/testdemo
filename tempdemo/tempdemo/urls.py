from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls', namespace='polls', app_name='polls')),
    url(r'^admin/', admin.site.urls),
]

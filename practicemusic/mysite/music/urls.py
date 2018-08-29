from django.conf.urls import url, include
from . import views

app_name = 'music'

urlpatterns = [
    #load for url
    url(r'^$', views.index, name='index'),
    #load for url/music
    url(r'^music/$', views.info, name='info'),
    #load for url/music/album_id
    url(r'^music/(?P<album_id>[0-9]+)/$', views.details, name='details'),
]






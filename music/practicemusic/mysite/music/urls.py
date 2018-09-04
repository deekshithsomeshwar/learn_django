from django.conf.urls import url, include
from . import views

app_name = 'music'





# FOR CLASS BASED VIEWS

urlpatterns = [

    url(r'^$',views.InfoView.as_view(), name='info'),
    url(r'^music/(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='details'),
    #/music/album/add/
    url(r'^album/add/$',views.AlbumCreate.as_view(),name='album-add'),

    #/music/album/2/
    url(r'^album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name='album-update'),

    #/music/album/2/delete
    url(r'^album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name='album-delete'),

]
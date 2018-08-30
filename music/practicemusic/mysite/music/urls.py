from django.conf.urls import url, include
from . import views

app_name = 'music'





# FOR CLASS BASED VIEWS

urlpatterns = [
    url(r'^$',views.InfoView.as_view(), name='info'),
    url(r'^music/(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='details'),
]
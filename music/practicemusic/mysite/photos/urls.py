from django.conf.urls import url, include
from . import views


app_name = 'photos'

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='info'),

]
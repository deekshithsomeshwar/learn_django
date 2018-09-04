from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from . models import Album
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views.generic import TemplateView
# Create your views here.

class HomePage(TemplateView):
    template_name = 'photos/info.html'


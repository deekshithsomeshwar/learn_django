# from django.shortcuts import render
# from django.views.generic import TemplateView
# from django.shortcuts import render, get_object_or_404
# from . models import Album, Song
#
# # Create your views here.
#

# GENERIC VIEWS

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Album
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View


class InfoView(generic.ListView):
    template_name = 'music/info.html'
    context_object_name = 'all_album'
    # by default the name is object list
    #if not changed here using context, we need to change the same in info.html

    def get_queryset(self):
        return Album.objects.all()

class DetailsView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','logo']

class AlbumDelete(DeleteView):
    model = Album
    template_name = 'music/confirm_delete.html'
    success_url = reverse_lazy('music:info')





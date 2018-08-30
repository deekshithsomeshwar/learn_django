# from django.shortcuts import render
# from django.views.generic import TemplateView
# from django.shortcuts import render, get_object_or_404
# from . models import Album, Song
#
# # Create your views here.
#

# GENERIC VIEWS

from django.views import generic
from . models import Album


class InfoView(generic.ListView):
    template_name = 'info.html'
    context_object_name = 'all_album'
    # by default the name is object list
    #if not changed here using context, we need to change the same in info.html

    def get_queryset(self):
        return Album.objects.all()

class DetailsView(generic.DetailView):
    model = Album
    template_name = 'details.html'
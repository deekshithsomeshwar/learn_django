from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from . models import Album

# Create your views here.

def index(request):
    return render(request, 'index.html')

def info(request):
    all_album = Album.objects.all()
    return render(request, 'info.html', {'all_album': all_album})

def details(request, album_id):
    album = get_object_or_404(Album,pk=album_id)
    return render(request, 'details.html', {'album': album})

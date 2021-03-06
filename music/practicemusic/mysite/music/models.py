from django.db import models
from django.urls import reverse, reverse_lazy


# Create your models here.


class Album(models.Model):
    album_title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    logo = models.FileField()
    genre = models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse('music:details', kwargs={'pk':self.pk})

    def __str__(self):
        return self.album_title + '-' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=200)
    song_title = models.CharField(max_length=100)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

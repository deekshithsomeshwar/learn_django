from django.db import models
from django.urls import reverse, reverse_lazy

# Create your models here.


class Album(models.Model):
    album_title = models.CharField(max_length=20)
    album_image = models.FileField()
    created_by = models.CharField(max_length=50)
    created_date = models.DateField()


    def get_absolute_url(self):
        return reverse('photos:list', kwargs={'pk':self.pk})

    def __str__(self):
        return self.album_title+ '-' + self.created_by


class Images(models.Model):
    Image_name = models.ForeignKey(Album, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.location
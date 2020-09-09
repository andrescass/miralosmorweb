from django.db import models

# Create your models here.
class TagClass(models.Model):
    name = models.CharField(max_length=70, blank=True, default='')
    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=70, blank=True, default='')
    year = models.CharField(max_length=70, blank=True, default='')
    link = models.CharField(max_length=70, unique=True, blank=False, default='')
    words = models.CharField(max_length=70, blank=True, default='')
    mtags = models.ManyToManyField(TagClass, blank=True, related_name='movie_tags')
    def __str__(self):
        return self.name

class MovieList(models.Model):
    name = models.CharField(max_length=70, unique=True, blank=False, default='')
    description = models.CharField(max_length=70, blank=True, default='')
    img = models.CharField(max_length=70, blank=True, default='')
    by = models.CharField(max_length=70, blank=True, default='')
    words = models.CharField(max_length=70, blank=True, default='')
    tags = models.ManyToManyField(TagClass, blank=True, related_name='tags')
    movies = models.ManyToManyField(Movie, blank=True, related_name='Peliculas')
    
    def __str__(self):
        return self.name
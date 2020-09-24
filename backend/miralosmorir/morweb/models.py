from django.db import models

# Create your models here.
class TagClass(models.Model):
    name = models.CharField(max_length=70, blank=True, default='')
    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=150, blank=True, default='')
    year = models.CharField(max_length=70, blank=True, default='')
    link = models.CharField(max_length=100, unique=True, blank=False, default='')
    director = models.CharField(max_length=150, blank=True, default='')
    cast = models.CharField(max_length=500, blank=True, default='')
    imdb_id = models.CharField(max_length=70, unique=True, blank=False, default='')
    words = models.CharField(max_length=200, blank=True, default='')
    mtags = models.ManyToManyField(TagClass, blank=True, related_name='movie_tags')
    def __str__(self):
        return self.name

class MovieList(models.Model):
    name = models.CharField(max_length=70, unique=True, blank=False, default='')
    description = models.CharField(max_length=200, blank=True, default='')
    img = models.CharField(max_length=150, blank=True, default='')
    link = models.CharField(max_length=70, blank=True, default='')
    by = models.CharField(max_length=70, blank=True, default='')
    words = models.CharField(max_length=200, blank=True, default='')
    tags = models.ManyToManyField(TagClass, blank=True, related_name='tags')
    movies = models.ManyToManyField(Movie, blank=True, related_name='list')
    
    def __str__(self):
        return self.name

class CalendarCite(models.Model):
    title = models.CharField(max_length=150, blank=True, default='')
    start = models.CharField(max_length=150, blank=True, default='')
    end = models.CharField(max_length=150, blank=True, default='')
    discord = models.BooleanField(default=False)
    allDay = models.BooleanField(default=False)
    description = models.CharField(max_length=300, blank=True, default='')
    citeClass = models.CharField(max_length=75, blank=True, default='')

class MovieSearch(models.Model):
    movie_id = models.CharField(max_length=150, blank=True, default='')
    movie_name = models.CharField(max_length=150, blank=True, default='')
    search_field = models.CharField(max_length=150, blank=True, default='')
    movie_lists = models.CharField(max_length=300, blank=True, default='')
    movie_list_ids = models.CharField(max_length=150, blank=True, default='')
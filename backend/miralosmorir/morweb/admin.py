from django.contrib import admin
from .models import Movie, MovieList, TagClass

# Register your models here.
admin.site.register(Movie)
admin.site.register(MovieList)
admin.site.register(TagClass)
from django.contrib import admin
from .models import Movie, MovieList, TagClass

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'words')
    search_fields = ('name', 'words')

# Register your models here.
admin.site.register(Movie)
admin.site.register(MovieList)
admin.site.register(TagClass)
admin.site.register(MovieAdmin)
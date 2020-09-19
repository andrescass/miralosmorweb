from rest_framework import serializers 
from morweb.models import MovieList, Movie, CalendarCite, MovieSearch

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id',
        'name',
        'year',
        'cast',
        'imdb_id',
        'director',
        'link',
        'words',)

class MovieListSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many = True, read_only=True)
    class Meta:
        model = MovieList
        fields = ('id',
        'name',
        'description',
        'link',
        'img',
        'by',
        'words',
        'movies',
        'words',)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name')

class CiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarCite
        fields = ('id',
        'title',
        'start',
        'end',
        'description',
        'discord',
        'allDay')

class MovieSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSearch
        fields = (
        'movie_name',
        'movie_name',
        'search_field',
        'movie_lists',
        'movie_list_ids')
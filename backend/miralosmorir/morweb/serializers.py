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
        'words',
        'details',)

class MovieListSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many = True, read_only=True)
    class Meta:
        model = MovieList
        fields = ('id',
        'name',
        'description',
        'link',
        'ext_link',
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
        'allDay',
        'citeClass')

class MovieSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSearch
        fields = (
        'movie_id',
        'movie_name',
        'movie_director',
        'movie_year',
        'movie_detail',
        'search_field',
        'movie_lists',
        'movie_lists_links',
        'movie_list_ids')
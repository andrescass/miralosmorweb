from rest_framework import serializers 
from morweb.models import MovieList, Movie

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieList
        fields = ('name',
        'description',
        'img',
        'by',
        'words',
        'movies',
        'words',)

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('name',
        'link',
        'words',)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name')
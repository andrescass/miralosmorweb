from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.shortcuts import render
from django.views.generic import TemplateView

from morweb.models import MovieList, Movie, TagClass
from morweb.serializers import MovieListSerializer, MovieSerializer, TagSerializer
from rest_framework.decorators import api_view


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

@api_view(['GET', 'POST', 'DELETE'])
def movie_list_list(request):
    if request.method == 'GET':
        mlists = MovieList.objects.all()
        
        title = request.GET.get('name', None)
        if title is not None:
            mlists = mlists.filter(title__icontains=title)
        
        mlist_serializer = MovieListSerializer(mlists, many=True)
        return JsonResponse(mlist_serializer.data, safe=False)
    elif request.method == 'POST':
        mlist_data = JSONParser().parse(request)
        mlist_serializer = MovieListSerializer(data=mlist_data)
        if mlist_serializer.is_valid():
            mlist_serializer.save()
            return JsonResponse(mlist_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(mlist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        
        title = request.GET.get('name', None)
        if title is not None:
            movies = movies.filter(title__icontains=title)
        
        movie_serializer = MovieSerializer(movies, many=True)
        return JsonResponse(movie_serializer.data, safe=False)
    elif request.method == 'POST':
        movie_data = JSONParser().parse(request)
        movie_serializer = MovieSerializer(data=movie_data)
        if movie_serializer.is_valid():
            mname = movie_serializer.validated_data['name']
            movie_serializer.save()
            cmovie = Movie.objects.get(name = mname)
            mlists = MovieList.objects.all()
            for mt in cmovie[0].words.split(' '):
                for ml in mlists:
                    for t in ml.words.split(' '):
                        if t == mt.name:                            
                            ml.movies.add(cmovie)
                            ml.save()
            return JsonResponse(movie_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

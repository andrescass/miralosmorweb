from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.shortcuts import render
from django.views.generic import TemplateView

from morweb.models import MovieList, Movie, TagClass
from morweb.serializers import MovieListSerializer, MovieSerializer, TagSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

@csrf_exempt
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
        mlist = MovieListSerializer(data=mlist_data)
        if mlist.is_valid():
            ml = MovieList(name = mlist.validated_data['name'], 
            description = mlist.validated_data['description'],
            link = mlist.validated_data['link'],
            img = mlist.validated_data['img'],
            by = mlist.validated_data['by'],
            words = mlist.validated_data['words'])
            movies = Movie.objects.all()
            ml.save()
            for mw in ml.words.split(' '):
                for m in movies:
                    for mmw in m.words.split(' '):
                        if mw == mmw:
                            ml.movies.add(m)
                            ml.save()
            
            mlist = MovieListSerializer(ml)
            #mlist_serializer.save()
            return JsonResponse(mlist.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(mlist.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def movie_list_mmorvip(request):
    if request.method == 'GET':
        mlists = MovieList.objects.filter(words__icontains="morvip")
        mlist_serializer = MovieListSerializer(mlists, many=True)
        return JsonResponse(mlist_serializer.data, safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def movie_list_mmorir(request):
    if request.method == 'GET':
        mlists = MovieList.objects.filter(words__icontains="MiralosMorir")
        mlist_serializer = MovieListSerializer(mlists, many=True)
        return JsonResponse(mlist_serializer.data, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_list_detail(request, name):
    # ... tutorial = Tutorial.objects.get(pk=pk)
    try: 
        list_name = name.replace("_", " ")
        list_name_l = list_name.replace("-", " ")
        ml = MovieList.objects.filter(name = list_name_l) 
    except MovieList.DoesNotExist: 
        return JsonResponse({'message': 'The list does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        mlist = MovieListSerializer(ml[0]) 
        return JsonResponse(mlist.data)
    elif request.method == 'DELETE': 
        ml[0].delete() 
        return JsonResponse({'message': 'List was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_list_by_tag(request, tag):
    # ... tutorial = Tutorial.objects.get(pk=pk)
    ml_tag = []
    try: 
        mlists = MovieList.objects.filter(words__icontains=tag) 
    except MovieList.DoesNotExist: 
        return JsonResponse({'message': 'The list does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    for ml in mlists:
        for w in ml.words.split(' '):
            if w == tag:
                ml_tag.append(ml)
    if request.method == 'GET': 
        mlist = MovieListSerializer(mlists, many=True) 
        return JsonResponse(mlist.data, safe=False)

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
            newMovie = Movie(name = movie_serializer.validated_data['name'],
            year = movie_serializer.validated_data['year'],
            link = movie_serializer.validated_data['link'],
            words = movie_serializer.validated_data['words'])            
            newMovie.save()
            mlists = MovieList.objects.all()
            for mt in newMovie.words.split(' '):
                for ml in mlists:
                    for t in ml.words.split(' '):
                        if t == mt:                            
                            ml.movies.add(newMovie)
                            ml.save()
            return JsonResponse(movie_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, name):
    # ... tutorial = Tutorial.objects.get(pk=pk)
    try: 
        movie_name = name.replace("_", " ")
        movie_name_l = movie_name. replace("-", " ")
        m = Movie.objects.filter(name = movie_name_l) 
    except MovieList.DoesNotExist: 
        return JsonResponse({'message': 'The list does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        mlist = MovieSerializer(m[0]) 
        return JsonResponse(mlist.data)
    elif request.method == 'DELETE': 
        m[0].delete() 
        return JsonResponse({'message': 'Movie was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
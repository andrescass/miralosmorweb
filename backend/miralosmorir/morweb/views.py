from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q

from morweb.models import MovieList, Movie, TagClass, CalendarCite, MovieSearch
from morweb.serializers import MovieListSerializer, MovieSerializer, TagSerializer, CiteSerializer, MovieSearchSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

########  MOVIE LISTS #######

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

########  MOVIES #######

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
            words = movie_serializer.validated_data['words'],
            director = movie_serializer.validated_data['director'],
            cast = movie_serializer.validated_data['cast'],
            imdb_id = movie_serializer.validated_data['imdb_id'],
            details = movie_serializer.validated_data['details']) 
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
        return JsonResponse({'message': 'The movie does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        mlist = MovieSerializer(m[0])
        return JsonResponse(mlist.data)
    elif request.method == 'DELETE':
        m[0].delete()
        return JsonResponse({'message': 'Movie was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def movie_update_pk(request, pk):
    try:
        m = Movie.objects.get(id = pk)
    except MovieList.DoesNotExist:
        return JsonResponse({'message': 'The movie does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        movie_data = JSONParser().parse(request)
        movie_serializer = MovieSerializer(m, data=movie_data)
        if movie_serializer.is_valid():
            m.name = movie_serializer.validated_data['name']
            m.year = movie_serializer.validated_data['year'],
            m.director = movie_serializer.validated_data['director'],
            m.cast = movie_serializer.validated_data['cast'],
            m.words += " " + movie_serializer.validated_data['words']
            m.save()
            mlists = MovieList.objects.all()
            for mt in m.words.split(' '):
                for ml in mlists:
                    for t in ml.words.split(' '):
                        if t == mt:
                            ml.movies.add(m)
                            ml.save()
            return JsonResponse(movie_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def movie_update_id(request, imdb_id):
    try:
        m = Movie.objects.get(imdb_id = imdb_id)
    except MovieList.DoesNotExist:
        return JsonResponse({'message': 'The movie does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        movie_data = JSONParser().parse(request)
        movie_serializer = MovieSerializer(m, data=movie_data)
        if movie_serializer.is_valid():
            m.words += " " + movie_serializer.validated_data['words']
            m.save()
            mlists = MovieList.objects.all()
            for mt in m.words.split(' '):
                for ml in mlists:
                    for t in ml.words.split(' '):
                        if t == mt:
                            ml.movies.add(m)
                            ml.save()
            return JsonResponse(movie_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def movie_search(request, keyword):
    if request.method == 'GET':
        movies_d = Movie.objects.filter(director__icontains=keyword)
        movies_c = Movie.objects.filter(cast__icontains=keyword)
        return_list = []

        for m in movies_d:
            lists_names = ''
            lists_ids = ''
            lists = MovieList.objects.filter(movies__id = m.id)
            for l in lists:
                lists_names += l.name + ','
                lists_ids += str(l.id) + ','
            newMovie = MovieSearch(movie_id=m.id, 
            movie_name=m.name, 
            search_field='Director', 
            movie_lists=lists_names, 
            movie_list_ids=lists_ids)
            return_list.append(newMovie)
        for m in movies_c:
            lists_names = ''
            lists_ids = ''
            lists = MovieList.objects.filter(movies__id = m.id)
            for l in lists:
                lists_names += l.name + ','
                lists_ids += str(l.id) + ','
            newMovie = MovieSearch(movie_id=m.id, 
            movie_name=m.name, 
            search_field='Cast', 
            movie_lists=lists_names, 
            movie_list_ids=lists_ids)
            return_list.append(newMovie)
        movie_serializer = MovieSearchSerializer(return_list, many=True)
        return JsonResponse(movie_serializer.data, safe=False)

@api_view(['GET'])
def movie_search_director(request, keywords):
    if request.method == 'GET':
        return_list = []
        queries = keywords.split('-')
        criterions = Q(director__icontains=queries[0)
        for i in range(1, len(queries)):
            criterions &= Q(director__icontains=queries[i])
        
        movies = Movie.objects.filter(criterions)
        for m in movies:
            lists_names = ''
            lists_ids = ''
            lists = MovieList.objects.filter(movies__id = m.id)
            for l in lists:
                lists_names += l.name + ','
                lists_ids += str(l.id) + ','
            newMovie = MovieSearch(movie_id=m.id, 
            movie_name=m.name, 
            search_field='Director', 
            movie_lists=lists_names, 
            movie_list_ids=lists_ids)
            return_list.append(newMovie)
        movie_serializer = MovieSearchSerializer(return_list, many=True)
        return JsonResponse(movie_serializer.data, safe=False)



########  CALENDAR CITE #######
@api_view(['GET', 'POST', 'DELETE'])
def calendar_list(request):
    # GET list of cites, POST a new cite, DELETE all cites
    if request.method == 'GET':
        cites = CalendarCite.objects.all()
        cite_serializer = CiteSerializer(cites, many=True)
        return JsonResponse(cite_serializer.data, safe=False)
    elif request.method == 'POST':
        cite_data = JSONParser().parse(request)
        cite_serializer = CiteSerializer(data = cite_data)
        if cite_serializer.is_valid():
            cite_serializer.save()
            return JsonResponse(cite_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(cite_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = CalendarCite.objects.all().delete()
        return JsonResponse({'message': '{} Cites were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def calendar_detail(request, pk):
    # find cite by pk (id)
    try: 
        cite = CalendarCite.objects.get(pk=pk) 
    except CalendarCite.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    # GET / PUT / DELETE tutorial
    if request.method == 'GET': 
        cite_serializer = CiteSerializer(tutorial) 
        return JsonResponse(cite_serializer.data)
    elif request.method == 'PUT': 
        cite_data = JSONParser().parse(request) 
        cite_serializer = CiteSerializer(cite, data=cite_data) 
        if cite_serializer.is_valid(): 
            cite_serializer.save() 
            return JsonResponse(cite_serializer.data) 
        return JsonResponse(cite_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        cite.delete() 
        return JsonResponse({'message': 'Cite was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
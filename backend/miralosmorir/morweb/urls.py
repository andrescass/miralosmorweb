from django.conf.urls import url
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
 
from morweb import views
from rest_framework import routers
 
 
router = routers.DefaultRouter()

 
urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^api/movielists$', csrf_exempt(views.movie_list_list)),
    url(r'^api/movielists-morvip$', csrf_exempt(views.movie_list_mmorvip)),
    url(r'^api/movielists-mm$', csrf_exempt(views.movie_list_mmorir)),
    path('api/movielists/<name>', views.movie_list_detail),
    path('api/movieliststag/<tag>', views.movie_list_by_tag),
    url(r'^api/movies$', views.movie_list),
    path('api/movies/<name>', views.movie_detail),
]
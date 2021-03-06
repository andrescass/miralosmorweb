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
    path('api/movie/update_pk/<pk>', views.movie_update_pk),
    path('api/movie/update_id/<imdb_id>', views.movie_update_id),
    path('api/movie/search/<keyword>', views.movie_search),
    path('api/movie/search_director/<keywords>', views.movie_search_director),
    path('api/movie/search_name/<keywords>', views.movie_search_name),
    url(r'^api/calendar/all$', csrf_exempt(views.calendar_list)),
    path('api/calendar/cite/<pk>', views.calendar_detail),
    url(r'^api/calendar/newcite$', csrf_exempt(views.calendar_list)),
    path('api/calendar/updatecite/<pk>', views.calendar_detail),
    path('api/calendar/calendar/delcite/<pk>', views.calendar_detail),
    url(r'^api/calendar/daletealatoda$', csrf_exempt(views.calendar_list)),
]
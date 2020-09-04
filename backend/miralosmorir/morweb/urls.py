from django.conf.urls import url
from django.urls import path, include
 
from morweb import views
from rest_framework import routers
 
 
router = routers.DefaultRouter()

 
urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
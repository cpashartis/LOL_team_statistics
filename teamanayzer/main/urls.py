from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^', views.FrontView.as_view() ),
    #url(r'^summoner/summoner_name='), #pk
]

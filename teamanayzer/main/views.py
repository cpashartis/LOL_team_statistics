from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.urls import reverse

from .forms import SummonerNameForm

# Create your views here.

# Welcome sentence
#def index(request):
#	return HttpResponse("Hey Fucker, Put your summoner name !!")

class FrontView(generic.TemplateView):
	template_name = 'main/front.html'


######################################################
#NEEED TO CHANGE TO ACCEPT MULTIPLE HTML REQUESTS ####
######################################################
def get_name(request):
    if request.method == 'GET':
        url_full = request.get_full_path()
        split = url_full.split("=")
        summoner_name = split[-1]

    return render(request, 'main.html')
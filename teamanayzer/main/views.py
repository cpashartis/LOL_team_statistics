from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.urls import reverse

#from .forms import SummonerNameForm

# Create your views here.

# Welcome sentence
#def index(request):
#	return HttpResponse("Hey Fucker, Put your summoner name !!")

class FrontView(generic.TemplateView):
	template_name = 'main/front.html'

def get_name(request):
    # if this is a POST request we need to process the form data
    '''if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SummonerNameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('main:summonerstatistics'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SummonerNameForm()'''
    if request.method == 'GET':
        url_full = request.get_full_path()
        split = url_full.split("=")
        summoner_name = split[-1]

    return render(request, 'main.html')

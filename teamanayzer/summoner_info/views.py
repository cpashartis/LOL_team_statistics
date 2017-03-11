from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Welcome sentence
def index(request):
	return HttpResponse("Hey Fucker, Put your summoner name !!)



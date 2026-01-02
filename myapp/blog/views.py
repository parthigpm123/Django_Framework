from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
      return HttpResponse("Welcome to the Blog Index Page")

def detail(request):
      return HttpResponse("You're looking at blog")
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
      return render(request,'index.html')
#Dynamic URL handling with parameter
def detail(request, post_id):
       return render(request,'detail.html')

def old_url_redirect(request, post_id):
      return redirect('new_url')

def new_url(request):
      return HttpResponse("This is the new URL page.")
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from . import views

# Create your views here.
def index(request):
    return render(request, 'core/index.html')
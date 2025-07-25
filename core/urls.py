from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('about', views.index, name='about'),
    path('contact', views.index, name='contact'),
]

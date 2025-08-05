from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('home', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services_view, name='services'),  # ✅ Add this line
    path('contact/submit/', views.contact_view, name='contact_submit'),
]

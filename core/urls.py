from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('home', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact/', contact_view, name='contact'),
    path('services/', views.services_view, name='services'),  # ✅ Add this line
    path('contact/submit/', contact_view, name='contact_submit'),
]

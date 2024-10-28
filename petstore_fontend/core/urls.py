# We are in urls.py file of core app

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('dog_categories',views.dog_categories,name='dogcategories'),
    path('cat_categories',views.cat_categories,name='catcategories'),
    path('bird_categories',views.bird_categories,name='birdcategories'),
    path('pet_details',views.pet_details,name='petdetails'),
]

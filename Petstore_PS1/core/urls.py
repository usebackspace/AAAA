from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('dogcategories',views.dog_categories,name='dogcategories'),
]

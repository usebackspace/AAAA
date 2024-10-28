# We are in urls.py file of core app

from django.urls import path
from . import views

#------ To incude Media file ---------------
from django.conf import settings
from django.conf.urls.static import static
#-----------------------------------------------

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('dog_categories',views.dog_categories,name='dogcategories'),
    path('cat_categories',views.cat_categories,name='catcategories'),
    path('bird_categories',views.bird_categories,name='birdcategories'),
    path('pet_details/<int:id>/',views.pet_details,name='petdetails'),
]


#--------- THis is will add file to media folder -----------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
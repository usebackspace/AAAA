from django.shortcuts import render
from . models import Pet
# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


def dog_categories(request):
    dc = Pet.objects.filter(category='DOG')
    return render(request,'core/dog_categories.html',{'dc':dc})


def cat_categories(request):
    dc = Pet.objects.filter(category='CAT')
    return render(request,'core/cat_categories.html',{'dc':dc})


def bird_categories(request):
    return render(request,'core/bird_categories.html')

def pet_details(request,id):
    dc = Pet.objects.get(pk=id)
    return render(request,'core/pet_details.html',{'dc':dc})
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


def dog_categories(request):
    return render(request,'core/dog_categories.html')


def cat_categories(request):
    return render(request,'core/cat_categories.html')


def bird_categories(request):
    return render(request,'core/bird_categories.html')

def pet_details(request):
    return render(request,'core/pet_details.html')
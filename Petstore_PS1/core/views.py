from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def dog_categories(request):
    return render(request,'core/dogcategories.html')
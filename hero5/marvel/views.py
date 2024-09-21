from django.shortcuts import render

# Create your views here.
def spiderman(request):
    return render(request,'marvel/spiderman.html')
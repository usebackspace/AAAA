from django.shortcuts import render

# Create your views here.
def spiderman(request):
    context={'superhero':'spiderman'}
    return render(request,'marvel/spiderman.html',context)
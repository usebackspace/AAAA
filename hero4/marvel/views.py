from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def spiderman(request):
    return render(request,'marvel/spiderman.html')

def ironman(request):
    return HttpResponse('ironman')

def antman(request):
    return HttpResponse('antman')
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def batman(request):
    return render(request,'dc/batman.html')

def superman(request):
    return HttpResponse('I am a superman')

def flash(request):
    return HttpResponse('I am a flash')

def vector(request):
    return HttpResponse('I am a vector')

def wonderman(request):
    return HttpResponse('I am a wonderman')

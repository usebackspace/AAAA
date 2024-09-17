from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def superman(request):
    return HttpResponse('I am a superman')

def batman(request):
    return HttpResponse('I am a batman')

def flash(request):
    return HttpResponse('I am a flash')

def vector(request):
    return HttpResponse('I am a vector')

def wonderman(request):
    return HttpResponse('I am a wonderman')

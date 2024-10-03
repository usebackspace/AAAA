from django.shortcuts import render
from . forms import MarvelForm
# Create your views here.


def index(request):
    # mf= MarvelForm(initial={'name':'America'})
    mf= MarvelForm()
    return render(request,'core/index.html',{'mf':mf})
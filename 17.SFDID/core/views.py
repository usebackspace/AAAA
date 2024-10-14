from django.shortcuts import render,redirect
from .forms import MarvelForm
from . models import Marvel
def index(request):
    if request.method == 'POST':
        mf =MarvelForm(request.POST)
        if mf.is_valid():
            nm= mf.cleaned_data['name']        
            hn= mf.cleaned_data['heroic_name']
            Marvel(name = nm, heroic_name=hn).save()
            # return render(request,'core/success.html')
            return redirect('index')
    else:
        mf= MarvelForm()
    return render(request,'core/index.html',{'mf':mf})

def success(request):
    return render(request,'core/success.html')
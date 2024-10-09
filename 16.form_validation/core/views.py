from django.shortcuts import render,redirect
from .forms import MarvelForm

def index(request):
    if request.method == 'POST':
        mf =MarvelForm(request.POST)
        if mf.is_valid():
            print('name..',mf.cleaned_data['name'])
        
            # return render(request,'core/success.html')
            return redirect('success')
    else:
        mf= MarvelForm()
    return render(request,'core/index.html',{'mf':mf})

def success(request):
    return render(request,'core/success.html')
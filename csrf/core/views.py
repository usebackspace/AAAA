from django.shortcuts import render,redirect
from . forms import MarvelForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        mf= MarvelForm(request.POST)
        if mf.is_valid():
            name=mf.cleaned_data['name']
            print('name',mf.cleaned_data['name'])
            print('email',mf.cleaned_data['email'])
        mf= MarvelForm()
        return redirect('success/')
        # return render( request,'core/success.html',{'name':name})
    else:
        mf= MarvelForm()
    return render(request,'core/index.html',{'mf':mf})

def success(request):
    return render(request,'core/success.html')
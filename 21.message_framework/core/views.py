from django.shortcuts import render,redirect
from .models import Marvel
from .forms import MarvelForm
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method=='POST':
        mf =MarvelForm(request.POST)
        if mf.is_valid():
            mf.save()
            # messages.success(request,'New Avenger Added Successfully')
            messages.info(request,'New Avenger Added Successfully')
        return redirect('index')
    else:
        mf= MarvelForm()
        mm= Marvel.objects.all()
    return render(request,'core/index.html',{'mf':mf,'marvel':mm})


def delete(request,id):
    if request.method=='POST':
        mm = Marvel.objects.get(pk=id)
        mm.delete()
        return redirect('index')
    

def update(request,id):
    if request.method=='POST':
        mm=Marvel.objects.get(pk=id)
        mf= MarvelForm(request.POST,instance=mm)
        if mf.is_valid():
            mf.save()
    else:
        mm=Marvel.objects.get(pk=id)
        mf= MarvelForm(instance=mm)
    return render(request,'core/update.html',{'mf':mf})
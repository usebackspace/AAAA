from django.shortcuts import render,redirect
from .forms import Dc
from django.http import HttpResponseRedirect
# Create your views here.
def success(request):
    return render(request,'dc/success.html')


def superman(request):
    if request.method == 'POST':
        dc= Dc(request.POST)
        if dc.is_valid():
            name = dc.cleaned_data['name']
            heroic_name = dc.cleaned_data['heroic_name']
            print(name)
            print(heroic_name)
            # return render(request,'dc/success.html',{'villian':'Zod','dc':dc})
            # return HttpResponseRedirect('/dc/success/')
            return redirect('/dc/success/')
    else:
        dc =Dc()   
    return render(request,'dc/superman.html',{'villian':'Zod','dc':dc})

def batman(request):
    return render(request,'dc/batman.html',{'villian':'Bayne'})
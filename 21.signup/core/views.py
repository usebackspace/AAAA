from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import  SignUpForm

# Create your views here.
# def index(request):
#     if request.method == 'POST':
#         mf = UserCreationForm(request.POST)
#         if mf.is_valid():
#             mf.save()
#             messages.success(request,'Welcome to the Avenger')
#             return redirect('index')
#     else:

#         mf=UserCreationForm()
#     return render(request,'core/index.html',{'mf':mf})

def index(request):
    if request.method == 'POST':
        mf = SignUpForm(request.POST)
        if mf.is_valid():
            mf.save()
            messages.success(request,'Welcome to the Avenger')
            return redirect('index')
    else:

        mf=SignUpForm()
    return render(request,'core/index.html',{'mf':mf})


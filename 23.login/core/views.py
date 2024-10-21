from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import  SignUpForm
from django.contrib.auth import authenticate,login,logout


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            mf = SignUpForm(request.POST)
            if mf.is_valid():
                mf.save()
                messages.success(request,'Welcome to the Avenger')
                return redirect('signup')
        else:
            mf=SignUpForm()
        return render(request,'core/signup.html',{'mf':mf})
    else:
        return redirect('profile')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            mf = AuthenticationForm(request,data=request.POST)
            if mf.is_valid():
                u_username = mf.cleaned_data['username']
                u_password = mf.cleaned_data['password']
                user = authenticate(username=u_username,password=u_password)
                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            mf =AuthenticationForm()
        return render(request,'core/login.html',{'mf':mf})
    else:
        return redirect('profile')


def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'core/profile.html')
    else:
        return redirect('login')

def user_logout(request):
    logout(request)
    return redirect('login')
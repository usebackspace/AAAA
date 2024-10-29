from django.shortcuts import render,redirect
from . models import Pet
from . forms import RegistrationForm,AuthenticateForm,ChangePasswordForm,UserProfileForm,AdminProfileForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


def dog_categories(request):
    dc = Pet.objects.filter(category='DOG')
    return render(request,'core/dog_categories.html',{'dc':dc})


def cat_categories(request):
    dc = Pet.objects.filter(category='CAT')
    return render(request,'core/cat_categories.html',{'dc':dc})


def bird_categories(request):
    return render(request,'core/bird_categories.html')

def pet_details(request,id):
    dc = Pet.objects.get(pk=id)
    return render(request,'core/pet_details.html',{'dc':dc})


# =======================================================================================



def registration(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            mf = RegistrationForm(request.POST)
            if mf.is_valid():
                mf.save()
                messages.success(request,'Registration Successfull !!')
                return redirect('registration')    
        else:
            mf  = RegistrationForm()
        return render(request,'core/registration.html',{'mf':mf})
    else:
        return redirect('profile')

def log_in(request):
    if not request.user.is_authenticated:  # check whether user is not login ,if so it will show login option
        if request.method == 'POST':       # otherwise it will redirect to the profile page 
            mf = AuthenticateForm(request,request.POST)
            if mf.is_valid():
                name = mf.cleaned_data['username']
                pas = mf.cleaned_data['password']
                user = authenticate(username=name, password=pas)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        else:
            mf = AuthenticateForm()
        return render(request,'core/login.html',{'mf':mf})
    else:
        return redirect('profile')

def profile(request):
    if request.user.is_authenticated:  # This check wheter user is login, if not it will redirect to login page
        if request.method == 'POST':
            if request.user.is_superuser == True:
                mf = AdminProfileForm(request.POST,instance=request.user)
            else:
                mf = UserProfileForm(request.POST,instance=request.user)
            if mf.is_valid():
                mf.save()
                messages.success(request,'Profile Updated Successfully !!')
        else:
            if request.user.is_superuser == True:
                mf = AdminProfileForm(instance=request.user)
            else:
                mf = UserProfileForm(instance=request.user)
        return render(request,'core/profile.html',{'name':request.user,'mf':mf})
    else:                                                # request.user returns the username
        return redirect('login')

def log_out(request):
    logout(request)
    return redirect('home')


def changepassword(request):                                       # Password Change Form               
    if request.user.is_authenticated:                              # Include old password 
        if request.method == 'POST':                               
            mf =ChangePasswordForm(request.user,request.POST)
            if mf.is_valid():
                mf.save()
                update_session_auth_hash(request,mf.user)
                return redirect('profile')
        else:
            mf = ChangePasswordForm(request.user)
        return render(request,'core/changepassword.html',{'mf':mf})
    else:
        return redirect('login')
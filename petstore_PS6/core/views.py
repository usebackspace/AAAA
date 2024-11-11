from django.shortcuts import render,redirect,get_object_or_404
from . models import Pet,Cart,CustomerDetail
from . forms import RegistrationForm,AuthenticateForm,ChangePasswordForm,UserProfileForm,AdminProfileForm,CustomerForm
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
    

# ============================ Add To Cart ====================================

def add_to_cart(request,id):
    if request.user.is_authenticated:
        pet = Pet.objects.get(pk=id)
        user = request.user
        Cart(user=user,product=pet).save()
        messages.success(request,'Added to cart succcefully !')
        return redirect('petdetails', id)
    else:
        return redirect('login')


def view_cart(request):
    if request.user.is_authenticated:
        cart_items =Cart.objects.filter(user=request.user)
        return render(request,'core/view_cart.html',{'cart_items':cart_items,})
    else:
        return redirect('login')


def add_quantity(request,id):
    if request.user.is_authenticated:
        product = get_object_or_404(Cart,pk=id)
        product.quantity+=1
        product.save()
        return redirect('viewcart')
    else:
        return redirect('login')

def delete_quantity(request,id):
    if request.user.is_authenticated:
        product = get_object_or_404(Cart,pk=id)
        if product.quantity>1:
            product.quantity-=1
            product.save()
        return redirect('viewcart')
    else:
        return redirect('login')
    
def delete_cart(request,id):
    pet_cart =Cart.objects.get(pk=id)
    pet_cart.delete()
    return redirect('viewcart')

# ================================ Address Page =========================
def address(request):
    if request.method == 'POST':
            mf =CustomerForm(request.POST)
            if mf.is_valid():
                user=request.user                # user variable store the current user i.e steveroger
                name= mf.cleaned_data['name']
                address= mf.cleaned_data['address']
                city= mf.cleaned_data['city']
                state= mf.cleaned_data['state']
                pincode= mf.cleaned_data['pincode']  
                CustomerDetail(user=user,name=name,address=address,city=city,state=state,pincode=pincode).save()
                return redirect('address')           
    else:
        mf =CustomerForm()
        address = CustomerDetail.objects.filter(user=request.user)
    return render(request,'core/address.html',{'mf':mf,'address':address})


def delete_address(request,id):
    if request.method == 'POST':
        de = CustomerDetail.objects.get(pk=id)
        de.delete()
    return redirect('address')

# ============================== Checkout Page ==============================

def checkout(request):
    cart_items =Cart.objects.filter(user=request.user)
    total=0
    delhivery_charge=2000
    for item in cart_items:
        total+=(item.product.discounted_price*item.quantity)
        final_price =total+delhivery_charge
    address = CustomerDetail.objects.filter(user=request.user)
    return render(request,'core/checkout.html',{'total':total,'final_price':final_price,'address':address})
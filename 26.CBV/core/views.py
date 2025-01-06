from django.shortcuts import render
# from django.views.generic.base import View
from django.views import View
from .forms import MarvelForm
# Create your views here.
# ========== Function Based View ==========
# def fbv(request):
#     return render(request,'core/fbv.html')


def fbv(request,heroic_name):
    context={'name':'steve roger','hero':heroic_name}
    return render(request,'core/fbv.html',context)


def fbv_form(request):
    if request.method =='POST':
        mf= MarvelForm(request.POST)
        if mf.is_valid():
            print(mf.cleaned_data['name'])
        mf= MarvelForm()
    else:
        mf= MarvelForm()
    return render(request,'core/marvelform.html',{'mf':mf})

def fbv_template(request,template_name):
    # template_name='core/template1.html'
    context={'name':'This is function base view template'}
    return render(request,template_name,context)





#============ Class Based View =============

# class Cbv(View):
#     def get(self,request):
#         return render(request,'core/cbv.html')


class Cbv(View):
    heroic_name=''
    def get(self,request):
        context={'name':'steve roger','hero':self.heroic_name}
        return render(request,'core/cbv.html',context)
    

class CbvForm(View):
    def get(self,request):
        mf= MarvelForm()
        return render(request,'core/marvelform.html',{'mf':mf})
    
    def post(self,request):
        mf= MarvelForm(request.POST)
        if mf.is_valid():
            print(mf.cleaned_data['name'])
        mf= MarvelForm()
        return render(request,'core/marvelform.html',{'mf':mf})


class CbvTemplate(View):
    template_name=''
    def get(self,request):
        context={'name':'This is function CLASS view template'}
        return render(request,self.template_name,context)
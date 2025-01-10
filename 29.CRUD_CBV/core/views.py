from django.shortcuts import render,redirect
from .models import Marvel
from .forms import MarvelForm
from django.views.generic.base import TemplateView,RedirectView,View

# Create your views here.

class IndexView(TemplateView):
    template_name='core/index.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        mf= MarvelForm()
        mm= Marvel.objects.all()
        context={'mf':mf,'marvel':mm}
        return context
    
    
    def post(self,request):
        mf =MarvelForm(request.POST)
        if mf.is_valid():
            mf.save()
        return redirect('index')

class DeleteView(RedirectView):
    url='/'

    def get_redirect_url(self, *args, **kwargs):
        mm = Marvel.objects.get(pk=kwargs['id'])
        mm.delete()
        return super().get_redirect_url(*args, **kwargs)
    
class UpdateView(View):

    def get(self,request,id):
        mm=Marvel.objects.get(pk=id)
        mf= MarvelForm(instance=mm)
        return render(request,'core/update.html',{'mf':mf})
  
    def post(self,request,id):
        mm=Marvel.objects.get(pk=id)
        mf= MarvelForm(request.POST,instance=mm)
        if mf.is_valid():
            mf.save()
        return render(request,'core/update.html',{'mf':mf})
    


# def index(request):
#     if request.method=='POST':
#         mf =MarvelForm(request.POST)
#         if mf.is_valid():
#             mf.save()
#         return redirect('index')
#     else:
#         mf= MarvelForm()
#         mm= Marvel.objects.all()
#     return render(request,'core/index.html',{'mf':mf,'marvel':mm})


# def delete(request,id):
#     if request.method=='POST':
#         mm = Marvel.objects.get(pk=id)
#         mm.delete()
#         return redirect('index')
    

# def update(request,id):
#     if request.method=='POST':
#         mm=Marvel.objects.get(pk=id)
#         mf= MarvelForm(request.POST,instance=mm)
#         if mf.is_valid():
#             mf.save()
#     else:
#         mm=Marvel.objects.get(pk=id)
#         mf= MarvelForm(instance=mm)
#     return render(request,'core/update.html',{'mf':mf})
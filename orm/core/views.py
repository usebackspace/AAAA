from django.shortcuts import render
from . models import Marvel
# Create your views here.

def index(request):
    m = Marvel.objects.all()
    return render(request,'core/index.html',{'marvel':m})
from django.shortcuts import render,redirect

def index(request):
    
    return render(request,'core/index.html')

# def product(request,id):
#     print(type(id))
#     return render(request,'core/product.html',{'id':id})


def product(request,id,sub_id):
    print(type(id))
    return render(request,'core/product.html',{'id':id,'sub':sub_id})
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('product/<int:id>',views.product,name='product'),
    # path('product/<int:id>/<sub_id>',views.product,name='product'),
    
]


# Normally 2 fields is used for dynamic url
# <int:id> ,<str:id> 

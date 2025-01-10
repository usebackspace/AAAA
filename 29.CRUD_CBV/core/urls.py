from django.urls import path
from . import views
urlpatterns = [
    # path('',views.index,name='index'),
    # path('delete/<int:id>',views.delete,name='delete'),
    # path('update/<int:id>',views.update,name='update'),
    
    path('',views.IndexView.as_view(),name='index'),
    path('delete/<int:id>',views.DeleteView.as_view(),name='delete'),
    path('update/<int:id>',views.UpdateView.as_view(),name='update'),
]

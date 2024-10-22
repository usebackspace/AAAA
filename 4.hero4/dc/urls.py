from django.urls import path
from . import views
urlpatterns = [
    path('superman/',views.superman),
    path('batman/',views.batman),
    path('flash/',views.flash),
    path('wonderman/',views.wonderman),
    path('vector/',views.vector),
]

from django.urls import path
from . import views
urlpatterns = [
    path('superman/',views.superman),
    path('batman/',views.batman),
    path('success/',views.success)
]

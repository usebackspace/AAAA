from django.urls import path
from . import views
urlpatterns = [
    # path('',views.TemplateView.as_view(template_name='core/index.html')),  # without defining class we can render template
    path('',views.IndexView.as_view()), 

    # path('about/',views.TemplateView.as_view(template_name='core/about.html')),
    # path('about/',views.AboutView.as_view()),
    # path('about/',views.AboutView.as_view()),
    path('about/',views.AboutView.as_view(extra_context={'heroic_name':'captain america'})),
]

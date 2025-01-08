from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):      # In this class we are inherting TemplateView
    template_name='core/index.html'

class AboutView(TemplateView):
    template_name='core/about.html'      # this attribute used to render template

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        # context={'name':'steve roger'}   # this will not pass the extra context
        context['name']='steve roger'   # we have to use this format for passing the extra context
        print(kwargs)
        return context
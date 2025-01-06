from django.urls import path
from . import views
urlpatterns = [
    # path('fbv/',views.fbv,name='fbv'),
    path('fbv/',views.fbv,{'heroic_name':'captain america'},name='fbv'),
    path('fbvform/',views.fbv_form,name='fbvform'),
    # path('fbvtemplate1/',views.fbv_template,name='fbvtemplate1'),
    path('fbvtemplate1/',views.fbv_template,{'template_name':'core/template1.html'},name='fbvtemplate1'),
    path('fbvtemplate2/',views.fbv_template,{'template_name':'core/template2.html'},name='fbvtemplate2'),

    # path('cbv/',views.Cbv.as_view(),name='cbv'),
    path('cbv/',views.Cbv.as_view(heroic_name='captain america'),name='cbv'),
    path('cbvform/',views.CbvForm.as_view(),name='cbvform'),
    path('cbvtemplate1/',views.CbvTemplate.as_view(template_name='core/template1.html'),name='cbvtemplate1'),
    path('cbvtemplate2/',views.CbvTemplate.as_view(template_name='core/template2.html'),name='cbvtemplate2'),
]

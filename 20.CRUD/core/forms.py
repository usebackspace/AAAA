from django import forms
from .models import Marvel
class MarvelForm(forms.ModelForm):

    class Meta:
        model = Marvel
        fields ='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control col-auto'}),
            'heroic_name':forms.TextInput(attrs={'class':'form-control  '})
        }
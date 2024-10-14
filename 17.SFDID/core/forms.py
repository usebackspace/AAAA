from django import forms
    
class MarvelForm(forms.Form):
    name = forms.CharField()
    heroic_name = forms.CharField()

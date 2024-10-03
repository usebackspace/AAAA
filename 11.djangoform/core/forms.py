from django import forms

class MarvelForm(forms.Form):
    name =forms.CharField()
    email = forms.EmailField()
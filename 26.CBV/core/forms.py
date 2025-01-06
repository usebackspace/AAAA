from django import forms

class MarvelForm(forms.Form):
    name = forms.CharField(max_length=50)
from django import forms

class Dc(forms.Form):
    name = forms.CharField(error_messages={'required':'Please enter the name'})
    heroic_name =forms.CharField()

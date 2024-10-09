from django import forms
from django.core import validators

def start_with_a(val):
    x=val[0]
    if x.isdigit():
        raise forms.ValidationError('Enter Name that starts with alphabets')
    
    print(len(val))
    if len(val)>5:
        raise forms.ValidationError('Enter name less than 5 letters')
    
class MarvelForm(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(5)])
    name = forms.CharField(validators=[start_with_a])
    

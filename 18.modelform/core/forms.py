from django import forms
from . models import Marvel

# class MarvelForm(forms.Form):
#     name = forms.CharField()
#     heroic_name = forms.CharField()


class MarvelForm(forms.ModelForm):
    # name = forms.CharField(max_length=30) # This name field has highest priority compare to field define in  Marvel model

    class Meta:
        model = Marvel
        fields = ['name','heroic_name']
        labels = {'name':'Full Name'}
        error_messages={
            'name':{'required':'Enter proper name'},
            'heroic_name':{'required':'Enter Proper Heroic name'}
        }

        widgets ={
            # 'name': forms.PasswordInput(),
            'heroic_name':forms.TextInput(attrs={'class':'form-control '})
        }
        
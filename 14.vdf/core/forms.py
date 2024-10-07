from django import forms

class MarvelForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

    def clean_name(self):

        validate_name = self.cleaned_data['name']
        print('validate name',validate_name)

        if len(validate_name)>5:
            raise forms.ValidationError('Enter Value less than 5')
        return validate_name
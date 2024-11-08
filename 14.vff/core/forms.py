from django import forms

class MarvelForm(forms.Form):
    name = forms.CharField(error_messages={'required':'Please Enter your Name'})
    email = forms.EmailField()


    # for validation each field, we have to create function (clean_fieldName) of each field.
    # def clean_name(self):
    #     validate_name =self.cleaned_data['name']

    #     if len(validate_name)>5:
    #         raise forms.ValidationError('Enter the Name Less than 5 words')

# =======================================================================================
    # for validation of multiple field, we have to create inbuilt clean function .

    def clean(self):
        cleaned_data = super().clean()

        validate_name =cleaned_data['name']

        validate_email = cleaned_data['email']

        if len(validate_name)>5:
            raise forms.ValidationError('Enter the Name Less than 5 words')
        
        if len(validate_email)>8:
            raise forms.ValidationError('Enter the proper mail address ')
        
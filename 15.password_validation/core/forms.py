from django import forms

class MarvelForm(forms.Form):
    name = forms.CharField(error_messages={'required':'Please Enter your Name'})
    email = forms.EmailField()
    password =forms.CharField(widget=forms.PasswordInput())
    confirm_password =forms.CharField(widget=forms.PasswordInput())


    def clean(self):
        cleaned_data= super().clean()

        val_pass =cleaned_data['password']
        val_con_pass =cleaned_data['confirm_password']

        if val_pass != val_con_pass:
            raise forms.ValidationError('Password Doesn"t match')
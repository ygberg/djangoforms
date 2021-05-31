from django import forms
from .models import UserBase


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label='Enter Username',help_text='required')
    email = forms.EmailField(label='email', required=True,error_messages={'required':'email is needed for validation'})
    password1 =forms.CharField(label='password'widget=forms.PasswordInput)
    password2 =forms.CharField(label='retype password' widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name','email')
        



class Users_form(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255,widget=forms.PasswordInput)

       
class Notbot(forms.Form):
    first_name = forms.CharField(label=(''), max_length=255)
    email = forms.EmailField()

from django import forms
import random

class Basic_forms(forms.Form):

    eman = forms.CharField(label=("Name"), max_length=255)
    liaem = forms.EmailField(label=('Email'))
    txet = forms.CharField(label=('Text'),widget=forms.Textarea)
    
class Notbot(forms.Form):
    first_name = forms.CharField(label=(''), max_length=255)
    email = forms.EmailField()
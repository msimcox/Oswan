from django import forms
from .models import Motorcycle

class MotoForm(forms.ModelForm):
    class Meta:
        model = Motorcycle
        fields = ['name', 'year', 'size', 'image']

class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
from django import forms
from .models import Motorcycle

class MotoForm(forms.ModelForm):
    class Meta:
        model = Motorcycle
        fields = ['name', 'year', 'size', 'image']


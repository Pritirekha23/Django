from django import forms
from .models import Enquire


class Enquireform(forms.ModelForm):
    class Meta:
        model = Enquire
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 250px;', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'width: 250px;', 'placeholder': 'Enter your email'}),
            'msg': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 150px; width: 250px;', 'placeholder': 'Enter your message'}),
        }

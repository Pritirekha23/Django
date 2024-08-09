from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
       

class StudentsigninForm(forms.Form):
    email=forms.CharField()
    password=forms.CharField()
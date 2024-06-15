from django import forms

class StudentForm(forms.Form):
    name=forms.CharField(required=False)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
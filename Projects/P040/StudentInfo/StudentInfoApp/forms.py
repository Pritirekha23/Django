from django import forms

class EducationForm(forms.Form):
    college=forms.CharField()
    degree=forms.CharField()
    mark=forms.IntegerField()

class PersonalForm(forms.Form):
    name=forms.CharField()
    address=forms.CharField()
    email=forms.EmailField()

class ExtracurForm(forms.Form):
    fav_actor=forms.CharField()
    fav_flower=forms.CharField()
    
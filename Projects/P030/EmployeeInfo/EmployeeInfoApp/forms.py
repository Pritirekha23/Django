from django import forms

class EmployeeForm(forms.Form):
    name=forms.CharField()
    desg=forms.CharField()
    age=forms.IntegerField()
    sal=forms.FloatField()
    address=forms.CharField()
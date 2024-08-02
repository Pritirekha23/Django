from django import forms

class AddProductForm(forms.Form):
    Product_Name=forms.CharField()
    Quantity=forms.IntegerField()

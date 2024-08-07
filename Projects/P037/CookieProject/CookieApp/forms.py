from django import forms

class NameForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
    )

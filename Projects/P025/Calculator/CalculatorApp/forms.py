from django import forms

class CalculatorForm(forms.Form):
    num1=forms.IntegerField(label='Number 1', widget=forms.TextInput(attrs={'placeholder': 'Enter 1st number'}))
    num2=forms.IntegerField(label='Number 2',widget=forms.TextInput(attrs={'placeholder': 'Enter 2nd number'}))
    symbol = forms.CharField(label='Operation', max_length=1, widget=forms.TextInput(attrs={'placeholder': 'Enter math symbol (+, -, *, /)'}))
    
    




    # Symbol_choice = [
    #     ('addition', '+'),
    #     ('subtraction', '-'),
    #     ('multiplication', '*'),
    #     ('division', '/'),
    # ]
    # symbol = forms.ChoiceField(choices=Symbol_choice, label='Operations')


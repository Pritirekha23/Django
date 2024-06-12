from django import  forms 

class  Student_form(forms.Form):
    name=forms.CharField()
    roll_no=forms.IntegerField()
    age=forms.IntegerField()
    email=forms.EmailField()
    mark=forms.IntegerField()
    college=forms.CharField()

from django import  forms 

class  Studentform(forms.Form):
    name=forms.CharField()
    roll_no=forms.IntegerField()
    age=forms.IntegerField()
    email=forms.EmailField()
    mark=forms.IntegerField()
    college=forms.CharField()
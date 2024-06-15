from django import  forms 

class  Employeedetails(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()
    

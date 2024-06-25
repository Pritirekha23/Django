from django import forms


class StudentForm(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    mark=forms.IntegerField()

    def clean(self):
        d=super().clean()
        name=d['name']
        age=d['age']
        mark=d['mark']

        if len(name)<2 or len(name)>16:
            raise forms.ValidationError('Name length must be in between 2 and 16')
        if age<18:
            raise forms.ValidationError('Age must be between 18')
        if mark<60:
            raise forms.ValidationError('mark must be greate than 60')



















   
          
  



    


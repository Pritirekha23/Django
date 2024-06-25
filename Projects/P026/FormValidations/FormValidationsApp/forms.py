from django import forms

class StudentForm(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    mark=forms.IntegerField()
    # validations logic for each field
    def clean_name(self):
        name=self.cleaned_data['name']
        if len(name)>=2 and len(name)<=16:
            return name
        else:
            raise forms.ValidationError('Name length must be 2 to 16 charachter long')
        
    def clean_age(self):
        age = self.cleaned_data['age']
        if age >= 18 and age <= 23:
            return age
        else:
            raise forms.ValidationError('Age must be between 18 to 23')

    def clean_mark(self):
        mark = self.cleaned_data['mark']
        if mark >= 60 and mark <= 100:
            return mark
        else:
            raise forms.ValidationError('Mark must be between 60 and 100')
        


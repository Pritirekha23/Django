from django import forms
from django.core import validators

#ex-1
#in-built validators
# class StudentForm(forms.Form):
#     name=forms.CharField(validators=[validators.MinLengthValidator(2),validators.MaxLengthValidator(16)])
#     age=forms.IntegerField()
#     mark=forms.IntegerField()

#ex-2
#Custom validations with inbuilt validators
#Rule 1: Name length must be greater than or equal to 2 and less than or equal16.
#Rule 2: Second letter must be ‘u’
# class StudentForm(forms.Form):
#     name=forms.CharField(validators=[validators.MinLengthValidator(2),validators.MaxLengthValidator(16)])
#     age=forms.IntegerField()
#     mark=forms.IntegerField()


#     def clean_name(self):
#         name=self.cleaned_data['name']
#         if name[1]=='u' or name[1]=='U':
#             return name
#         else:
#             raise forms.ValidationError('The second character of name must be u or U')

#ex-3( inbuilt validators)
#Rule: Mark must be greater than 50 and less than or equal to 100.
# class StudentForm(forms.Form):
#     name=forms.CharField()
#     age=forms.IntegerField()
#     mark=forms.IntegerField(validators=[validators.MinValueValidator(50),validators.MaxValueValidator(100)])

#ex-4 ( inbuilt validators)
#Rule:validate email.
# class StudentForm(forms.Form):
#     name=forms.CharField()
#     age=forms.IntegerField()
#     mark=forms.IntegerField()
#     email=forms.EmailField(validators=[validators.EmailValidator()])


#ex-5( inbuilt validators with custom validators using validators parameter)
#Rule 1: Name length must be greater than or equal to 2 and less than or equal16.
#Rule 2: Second letter must be ‘u’

def email_specific(email):
    before_special,after_special = email.split('@')
    if len(before_special) > 10:
        raise forms.ValidationError('The part before @ must not exceed 10 characters.')
    
class StudentForm(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    mark=forms.IntegerField()
    email=forms.EmailField(validators=[validators.EmailValidator(),email_specific])
    





















    # phone=forms.IntegerField()
    # email=forms.EmailField()
    # adhar_number=forms.IntegerField()
    # address=forms.CharField(widget=forms.Textarea,max_length=30,help_text='maximun 30 char')
    # upload_cv=forms.FileField(required=False)
    # password=forms.CharField(widget=forms.PasswordInput)

   
          
  



    


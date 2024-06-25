from django import forms

class StudentForm(forms.Form):
    name=forms.CharField()
    phone=forms.IntegerField()
    email=forms.EmailField()
    adhar_number=forms.IntegerField()
    address=forms.CharField(widget=forms.Textarea,max_length=30,help_text='maximun 30 char')
    upload_cv=forms.FileField(required=False)
    password=forms.CharField(widget=forms.PasswordInput)

    # validations logic for name
    def clean_name(self):
        name=self.cleaned_data['name']
        if len(name)>=2 and len(name)<=16 and name.isalpha():
            return name
        else:
            raise forms.ValidationError('Name length must be 2 to 16 charachter long')
          
    # Validation logic for phone number
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone_str = str(phone)
        if len(phone_str) == 10 and phone_str.isdigit():
            return phone
        else:
            raise forms.ValidationError('Phone number must be 10 digits long')     
       
    # Validation logic for email
    # def clean_email(self):
    #     email=self.cleaned_data['email']
    #     email_lower=email.lower()
    #     return email_lower
    
    #Validation logic for adhar_number 
    def clean_adhar_number(self):
        adhar_number=self.cleaned_data['adhar_number']
        adhar_str=str(adhar_number)
        if len(adhar_str)==12 and adhar_str.isdigit():
            return adhar_number
        else:
            raise forms.ValidationError('Adhar number must be 12 digits long')
        
    # Validation logic for address 
    def clean_address(self):
        address = self.cleaned_data['address']
        if len(address) <= 30:
            return address
        else:
            raise forms.ValidationError('Address length must not exceed 30 characters')
        
   
    # validations logic for password
    

    



    


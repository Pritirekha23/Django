from django import forms

class StudentForm(forms.Form):
       name=forms.CharField()
       age=forms.IntegerField()
       email=forms.EmailField()
       mark=forms.IntegerField()
       college=forms.CharField()
    # name=forms.CharField(required=False)
    # age=forms.IntegerField(label_suffix="")
    # mark=forms.IntegerField()
    # email=forms.CharField(required=False,label="Mail-Id")
    # country=forms.CharField(initial='India',disabled=True)
    # bio=forms.CharField(widget=forms.Textarea,help_text='maximun 120 char',max_length=120)
    # upload_cv=forms.FileField()
    # upload_photo=forms.ImageField()
    # iagree=forms.CharField(widget=forms.CheckboxInput)
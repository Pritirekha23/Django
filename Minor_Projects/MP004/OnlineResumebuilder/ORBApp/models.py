from django.db import models
from django.core.validators import validate_email

class Resume(models.Model):
    name=models.CharField(max_length=50)
    desg=models.CharField(max_length=50)
    email=models.EmailField(validators=[validate_email])
    mob_number=models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    linkedin_id=models.URLField(null=True,blank=True)
    github_id=models.URLField(null=True,blank=True)
    profile_pic=models.ImageField(upload_to='profile_pic/')
    summary = models.TextField()
    designation=models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)
    years_worked=models.CharField(max_length=50)
    college_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    skills = models.TextField()
    languages = models.TextField()
        

from django.db import models
from django.core.validators import validate_image_file_extension


class Profile(models.Model):
    name=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    profile_pic=models.ImageField(upload_to='images/', validators=[validate_image_file_extension])
    email=models.EmailField()
    mark=models.IntegerField()
    
    def __str__(self):
        return self.name


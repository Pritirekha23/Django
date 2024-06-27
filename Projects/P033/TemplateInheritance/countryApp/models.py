from django.db import models
from django.core.validators import validate_image_file_extension

class Indiaplaces(models.Model):
    i_name=models.CharField(max_length=30)
    i_pic=models.ImageField(upload_to='images/', validators=[validate_image_file_extension])
    i_desc=models.CharField(max_length=100) 
    def __str__(self):
        return self.i_name
class Usaplaces(models.Model):
    us_name=models.CharField(max_length=30)
    us_pic=models.ImageField(upload_to='images/', validators=[validate_image_file_extension])
    us_desc=models.CharField(max_length=100) 
    def __str__(self):
        return self.us_name
class Ukplaces(models.Model):
    uk_name=models.CharField(max_length=30)
    uk_pic=models.ImageField(upload_to='images/', validators=[validate_image_file_extension])
    uk_desc=models.CharField(max_length=100) 
    def __str__(self):
        return self.uk_name
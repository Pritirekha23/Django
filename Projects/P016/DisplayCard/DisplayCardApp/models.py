from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    mark=models.IntegerField()
    email=models.EmailField()
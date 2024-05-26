from django.db import models

# Create your models here.
class Mobile(models.Model):
    name=models.CharField(max_length=30)
    brand=models.CharField(max_length=30)
    price=models.IntegerField()
   
    def __str__(self):
       return self.name
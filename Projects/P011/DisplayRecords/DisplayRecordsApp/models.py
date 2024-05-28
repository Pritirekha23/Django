from django.db import models

# Create your models here.
class Shirts(models.Model):
    brand=models.CharField(max_length=30)
    price=models.IntegerField()
    color=models.CharField(max_length=30)

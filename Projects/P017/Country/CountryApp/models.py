from django.db import models

# Create your models here.
class Country(models.Model):
    country_name=models.CharField(max_length=30)
    capital_name=models.CharField(max_length=30)
    population  =models.IntegerField()
    Readmore   =models.CharField(max_length=30)
    description = models.TextField() 

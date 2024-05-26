from django.db import models

# Create your models here.
class Mobile(model.Models):
    name=models.CharField(max_length=30)
    brand=models.CharField(max_length=30)
    price=models.IntegerField()

from django.db import models

# Create your models here.
class Tshirt(models.Model):
    name=models.CharField(max_length=20)
    brand=models.CharField(max_length=20)
    price=models.IntegerField()
    color=models.CharField(max_length=20)
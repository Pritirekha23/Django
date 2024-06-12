from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=50)
    capital_name = models.CharField(max_length=50)
    population = models.PositiveIntegerField()
    heading = models.CharField(max_length=200)
    readmore = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.country_name
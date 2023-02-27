# predict/models.py
from django.db import models

class House(models.Model):
    zipcode = models.CharField(max_length=10)
    view = models.IntegerField()
    grade = models.IntegerField()
    sqft_living = models.IntegerField()
    bathrooms = models.FloatField()
    waterfront = models.IntegerField()
    sqft_above = models.IntegerField()
    sqft_basement = models.IntegerField()
    sqft_living15 = models.IntegerField()
    days_since_reference_date = models.IntegerField()

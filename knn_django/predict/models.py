from django.db import models

class HousePrice(models.Model):
    zipcode = models.IntegerField()
    view = models.IntegerField()
    grade = models.IntegerField()
    sqft_living = models.FloatField()
    bathrooms = models.FloatField()
    waterfront = models.IntegerField()
    sqft_above = models.IntegerField()
    sqft_basement = models.IntegerField()
    sqft_living15 = models.IntegerField()
    days_since = models.IntegerField()
    predicted_price = models.FloatField(null=True)

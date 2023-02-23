from django import forms

class HouseForm(forms.Form):
    zipcode = forms.CharField(max_length=5)
    view = forms.IntegerField(min_value=0, max_value=4)
    grade = forms.IntegerField(min_value=1, max_value=13)
    sqft_living = forms.FloatField(min_value=0)
    bathrooms = forms.FloatField(min_value=0)
    waterfront = forms.IntegerField(min_value=0, max_value=1)
    sqft_above = forms.FloatField(min_value=0)
    sqft_basement = forms.FloatField(min_value=0)
    sqft_living15 = forms.FloatField(min_value=0)
    days_since_reference_date = forms.IntegerField(min_value=0)
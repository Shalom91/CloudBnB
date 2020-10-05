from django.db import models

# Create your models here.
class Property(models.Model):
    description_text = models.CharField(max_length=200)
    property_pictures = models.ImageField()
    city = models.CharField(max_length=50)
    suburb = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    max_number_of_guest = models.IntegerField()
    price_per_night_one_guest = models.DecimalField(max_digits=6, decimal_places=2)
    
    

from django.db import models

from validators.validators import minimum_two_char_validator, car_year_validator, car_price_validator


# Create your models here.


class CarsModel(models.Model):
    CAR_CHOICES = [
        ('SC', 'Sports Car'),
        ('PK', 'Pickup'),
        ('MB', 'Minibus'),
        ('OR', 'Other'),

    ]
    type = models.CharField(blank=False, null=False, max_length=10, choices=CAR_CHOICES)
    model = models.CharField(blank=False, null=False, max_length=20, validators=[minimum_two_char_validator])
    year = models.IntegerField(blank=False, null=False, validators=[car_year_validator])
    image_url = models.URLField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False, validators=[car_price_validator])

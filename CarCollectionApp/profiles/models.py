from django.db import models

from validators.validators import minimum_two_char_validator, age_validator


# Create your models here.

class ProfileModel(models.Model):
    username = models.CharField(blank=False, null=False, max_length=10, validators=[minimum_two_char_validator])
    email = models.EmailField(blank=False, null=False)
    age = models.PositiveIntegerField(blank=False, null=False, validators=[age_validator])
    password = models.CharField(blank=False, null=False, max_length=30)
    first_name = models.CharField(blank=True, null=True, max_length=30)
    last_name = models.CharField(blank=True, null=True, max_length=30)
    profile_picture = models.URLField(blank=True, null=True)

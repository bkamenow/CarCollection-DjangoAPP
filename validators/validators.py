from django.core.exceptions import ValidationError


def minimum_two_char_validator(value):
    if len(value) < 2:
        raise ValidationError('The username must be a minimum of 2 chars')


def age_validator(value):
    if value < 18:
        raise ValidationError('Age cannot be below 18!')


def car_year_validator(value):
    if value < 1980 or value > 2049:
        raise ValidationError('Year must be between 1980 and 2049')


def car_price_validator(value):
    if value < 1:
        raise ValidationError('Price cannot be below 1!')

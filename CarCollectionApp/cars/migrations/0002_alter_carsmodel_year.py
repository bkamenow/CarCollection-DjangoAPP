# Generated by Django 4.2.2 on 2023-06-23 18:17

from django.db import migrations, models
import validators.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsmodel',
            name='year',
            field=models.IntegerField(validators=[validators.validators.car_year_validator]),
        ),
    ]

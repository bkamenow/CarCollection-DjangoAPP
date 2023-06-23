# Generated by Django 4.2.2 on 2023-06-23 17:20

from django.db import migrations, models
import validators.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('SC', 'Sports Car'), ('PK', 'Pickup'), ('MB', 'Minibus'), ('OR', 'Other')], max_length=10)),
                ('model', models.CharField(max_length=20, validators=[validators.validators.minimum_two_char_validator])),
                ('year', models.CharField(validators=[validators.validators.car_year_validator])),
                ('image_url', models.URLField()),
                ('price', models.FloatField(validators=[validators.validators.car_price_validator])),
            ],
        ),
    ]
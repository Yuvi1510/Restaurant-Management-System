# Generated by Django 5.0.7 on 2024-07-24 06:41

import django.core.validators
import management.costume_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_carouselimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfo',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10), management.costume_validators.digits_validation]),
        ),
    ]

# Generated by Django 5.0.7 on 2024-07-23 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfo',
            name='logo',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]

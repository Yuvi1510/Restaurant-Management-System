# Generated by Django 5.0.7 on 2024-07-24 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_items_menu_dailyoffer_items_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyoffer',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
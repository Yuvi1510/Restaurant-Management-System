# Generated by Django 5.0.7 on 2024-07-31 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0024_remove_orderlist_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlist',
            name='item',
            field=models.CharField(default='', max_length=50),
        ),
    ]
# Generated by Django 5.0.7 on 2024-07-31 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0018_remove_order_order_completed_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='item',
            field=models.CharField(default='', max_length=50),
        ),
    ]

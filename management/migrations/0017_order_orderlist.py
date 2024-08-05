# Generated by Django 5.0.7 on 2024-07-31 06:09

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0016_userprofile_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('completed', models.BooleanField(default=False)),
                ('order_created_at', models.DateTimeField(auto_now_add=True)),
                ('order_completed_at', models.DateTimeField()),
                ('order_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('total', models.FloatField()),
                ('order_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.order')),
            ],
        ),
    ]
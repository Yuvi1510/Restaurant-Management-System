# Generated by Django 5.0.7 on 2024-07-28 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0013_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='Profile',
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-09 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0004_alter_location_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='phone_number',
        ),
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]

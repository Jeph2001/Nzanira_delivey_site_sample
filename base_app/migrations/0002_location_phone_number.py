# Generated by Django 4.2.3 on 2023-07-26 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='phone_number',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='base_app.signup'),
        ),
    ]
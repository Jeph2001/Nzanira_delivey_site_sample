# Generated by Django 4.2.3 on 2023-07-28 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_location_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('simple_description', models.CharField(max_length=50)),
                ('detailed_description', models.CharField(max_length=500)),
                ('image', models.ImageField(max_length=2080, upload_to='path/to/your/images/')),
            ],
        ),
        migrations.AlterField(
            model_name='location',
            name='phone_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.signup'),
        ),
    ]
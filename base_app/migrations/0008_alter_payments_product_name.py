# Generated by Django 4.2.3 on 2023-08-02 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0007_alter_payments_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='product_name',
            field=models.ForeignKey(default='details/<int:products_id>/', on_delete=django.db.models.deletion.CASCADE, to='base_app.products'),
        ),
    ]
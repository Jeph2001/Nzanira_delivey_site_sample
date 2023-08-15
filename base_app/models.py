from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Location(models.Model):
    city = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=500)
    # phone_number = models.ForeignKey(SignUp, related_name='phone' ,on_delete=models.CASCADE, default='1')
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.city
    

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    simple_description = models.CharField(max_length=50)
    detailed_description = models.CharField(max_length=500)
    image = models.ImageField(max_length=2080, upload_to='path/to/your/images/')


    def __str__(self):
        return self.product_name


class Payments(models.Model):
    names_of_client = models.CharField(max_length=200)
    momo_pay_code = models.CharField(max_length=10, default='260954')
    confirmation_code = models.CharField(max_length=10)
    # phone_number = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    # product_name = models.ForeignKey(Products, on_delete=models.CASCADE, default='deproduct.id/')
    phone_number = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)







   




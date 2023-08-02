from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

# Create your models here.

def validate_password_match(self, value):
    if value != self.password:
        raise ValidationError("Password is not matching. make sure you enter the correct passwords")



class SignUp(models.Model):
    full_name = models.CharField(max_length=200, null=False)
    phone_number = models.CharField(max_length=50, null=False)
    email_address = models.EmailField(max_length=200)
    password = models.CharField(max_length=10, validators=[MinLengthValidator(4)])

    
    def __str__(self):
        return self.phone_number



class Location(models.Model):
    city = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=500)
    phone_number = models.ForeignKey(SignUp, on_delete=models.CASCADE)


class Products(models.Model):
    product_name = models.CharField(max_length=100)
    simple_description = models.CharField(max_length=50)
    detailed_description = models.CharField(max_length=500)
    image = models.ImageField(max_length=2080, upload_to='path/to/your/images/')


class Payments(models.Model):
    names_of_client = models.CharField(max_length=200)
    momo_pay_code = models.CharField(max_length=10, default='260954')
    confirmation_code = models.CharField(max_length=10)
    phone_number = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    






   




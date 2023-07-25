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


class Location(models.Model):
    city = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=500)


   




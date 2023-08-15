from django import forms
from .models import  Location, Payments
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ['username', 'password']


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=20, label='Phone Number')
    password = forms.CharField(max_length=10, widget=forms.PasswordInput, label='Password')

class LocationForm(forms.ModelForm):


    class Meta:
        model = Location
        fields = "__all__"


class PaymentsForm(forms.ModelForm):


    class Meta:
        model = Payments
        fields = "__all__"

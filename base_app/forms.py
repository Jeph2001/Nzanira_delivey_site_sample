from django import forms
from .models import SignUp, Location


class SignUpForm(forms.ModelForm):

    
    class Meta:
        model = SignUp
        fields = "__all__"


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=20, label='Phone Number')
    password = forms.CharField(max_length=10, widget=forms.PasswordInput, label='Password')

class Location(forms.ModelForm):


    class Meta:
        model = Location
        fields = "__all__"
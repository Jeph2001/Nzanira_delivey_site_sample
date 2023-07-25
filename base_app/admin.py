from django.contrib import admin
from .models import SignUp

# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'email_address', 'password')


admin.site.register(SignUp, SignUpAdmin)

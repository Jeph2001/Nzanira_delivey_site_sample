from django.contrib import admin
from .models import SignUp, Location

# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'email_address', 'password')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'coordinates')


admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Location, LocationAdmin)

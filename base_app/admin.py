from django.contrib import admin
from .models import Location, Products, Payments, SignUp

# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'email_address', 'password')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'coordinates', 'phone_number')
    


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'simple_description', 'detailed_description', 'image')


class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('names_of_client', 'momo_pay_code', 'confirmation_code', 'phone_number')


admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Payments, PaymentsAdmin)

from django.contrib import admin
from .models import Location, Products, Payments

# Register your models here.



class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'coordinates')
    


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'simple_description', 'detailed_description', 'image')


class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('names_of_client', 'momo_pay_code', 'confirmation_code', 'phone_number')



admin.site.register(Location, LocationAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Payments, PaymentsAdmin)

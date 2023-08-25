from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Products, Payments, Location


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):

    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Location
        fields = ['city', 'coordinates', 'url']
    




class UserSerializers(serializers.ModelSerializer):
    # location = serializers.PrimaryKeyRelatedField(many=True, queryset=Location.objects.all())


    class Meta:
        model = User
        fields = ['id', 'username', 'password']



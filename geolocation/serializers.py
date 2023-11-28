# geolocation/serializers.py
from rest_framework import serializers
from .models import LocalDiscount

class LocalDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalDiscount
        fields = '__all__'

# compare/serializers.py
from rest_framework import serializers
from .models import ComparedProduct
from discounts.serializers import ProductSerializer

class ComparedProductSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = ComparedProduct
        fields = '__all__'

# discounts/serializers.py
from rest_framework import serializers
from .models import Product, Category, SubCategory
from ecommerce.serializers import StoreSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    sub_category = SubCategorySerializer()
    store = StoreSerializer()
    class Meta:
        model = Product
        fields = '__all__'


# class FilterSubCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubCategory
#         fields = "__all__"


# class FilterCategorySerializer(serializers.ModelSerializer):
#     subcategory = FilterSubCategorySerializer(many=True)

#     class Meta:
#         model = Category
#         fields = "__all__"
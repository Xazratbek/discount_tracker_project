# discounts/admin.py
from django.contrib import admin
from .models import Product, Category, SubCategory

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'original_price', 'discounted_price', 'sub_category', 'store', 'created_at')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
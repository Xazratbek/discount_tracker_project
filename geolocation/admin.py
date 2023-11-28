# geolocation/admin.py
from django.contrib import admin
from .models import LocalDiscount

@admin.register(LocalDiscount)
class LocalDiscountAdmin(admin.ModelAdmin):
    list_display = ('product', 'location', 'discount_percentage')
    list_filter = ('location',)
    search_fields = ('product__name',)

# ecommerce/admin.py
from django.contrib import admin
from .models import Store

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
    search_fields = ('name',)

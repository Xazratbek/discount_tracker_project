# compare/admin.py
from django.contrib import admin
from .models import ComparedProduct

@admin.register(ComparedProduct)
class ComparedProductAdmin(admin.ModelAdmin):
    list_display = ('user_comment', )

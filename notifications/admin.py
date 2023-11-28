# notifications/admin.py
from django.contrib import admin
from .models import PriceDropNotification

@admin.register(PriceDropNotification)
class PriceDropNotificationAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'product', 'threshold_price', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('user_profile__user__username', 'product__name')

# profiles/admin.py
from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_favorite_products', 'display_tracked_stores', 'notification_preferences', 'created_at')

    def display_favorite_products(self, obj):
        return ', '.join([str(product) for product in obj.favorite_products.all()])

    def display_tracked_stores(self, obj):
        return ', '.join([str(store) for store in obj.tracked_stores.all()])

admin.site.register(UserProfile, UserProfileAdmin)

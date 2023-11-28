# feeds/admin.py
from django.contrib import admin
from .models import ActivityFeed

@admin.register(ActivityFeed)
class ActivityFeedAdmin(admin.ModelAdmin):
    list_display = ('product', 'event_type', 'timestamp')
    list_filter = ('event_type',)
    search_fields = ('product__name',)

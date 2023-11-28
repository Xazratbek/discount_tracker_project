# feeds/serializers.py
from rest_framework import serializers
from .models import ActivityFeed

class ActivityFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityFeed
        fields = '__all__'

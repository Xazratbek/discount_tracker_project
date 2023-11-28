# notifications/serializers.py
from rest_framework import serializers
from .models import PriceDropNotification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceDropNotification
        fields = '__all__'

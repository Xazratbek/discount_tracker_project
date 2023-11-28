# recommendations/serializers.py
from rest_framework import serializers
from .models import UserRecommendation

class UserRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRecommendation
        fields = '__all__'

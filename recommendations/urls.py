# recommendations/urls.py
from django.urls import path
from .views import UserRecommendationsView

urlpatterns = [
    path('recommendations/', UserRecommendationsView.as_view(), name='user_recommendations'),
    # Add other recommendation-related URL patterns as needed
]

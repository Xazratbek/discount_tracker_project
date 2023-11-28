# feeds/urls.py
from django.urls import path
from .views import ActivityFeedListView

urlpatterns = [
    path('activity/feed/', ActivityFeedListView.as_view(), name='activity_feed_list'),
    # Add other feed-related URL patterns as needed
]

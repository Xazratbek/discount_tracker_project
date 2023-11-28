# feeds/views.py
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import ActivityFeed
from .serializers import ActivityFeedSerializer

class ActivityFeedListView(ListAPIView):
    queryset = ActivityFeed.objects.all()
    serializer_class = ActivityFeedSerializer
